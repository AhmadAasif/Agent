import os

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from app.gmail import (
    is_email_command,
    extract_email,
    create_gmail_url,
    generate_email_with_gemini
)

from app.youtube import youtube_bp


def create_app():

    app = Flask(__name__)
    CORS(app)

    # YouTube
    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    # Home
    @app.route("/")
    def home():
        return render_template("index.html")

    # HTML
    @app.route("/html")
    def html():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return jsonify({
            "status": "ok",
            "service": "nova AI Agent"
        })

    @app.route("/agent", methods=["POST"])
    def agent():

        try:
            data = request.get_json(silent=True) or {}
            command = data.get("command", "").strip()

            if not command:
                return jsonify({
                    "success": False,
                    "message": "command is required"
                }), 400

            if not is_email_command(command):
                return jsonify({
                    "success": False,
                    "message": "please give a small command"
                }), 400

            recipient = extract_email(command)

            email = generate_email_with_gemini(command)

            return jsonify({
                "success": True,
                "type": "email",
                "email_generated": True,
                "recipient": recipient,
                "subject": email["subject"],
                "body": email["body"],
                "gmail_url": create_gmail_url(
                    email["subject"],
                    email["body"],
                    recipient
                )
            })

        except Exception as e:

            return jsonify({
                "success": False,
                "message": str(e)
            }), 500

    return app
