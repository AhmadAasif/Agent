import os

from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS

from app.gmail import (
    is_email_command,
    extract_email,
    create_gmail_url,
    generate_email_with_gemini
)

from app.youtube import youtube_bp


def _render_nova_page():
    """Render the Nova UI with the embedded Luffy background visible above the page background."""
    html = render_template("index.html")

    # index.html contains the uploaded Luffy background as an embedded WebP.
    # Put the image and overlay in a predictable stacking order, then lift the UI
    # above both layers so the background cannot disappear behind the body.
    html = html.replace("z-index:-3", "z-index:0")
    html = html.replace("z-index:-2", "z-index:1")

    background_fix = """
<style id="nova-background-fix">
html, body { background: transparent !important; }
body:before { z-index: 0 !important; }
body:after { z-index: 1 !important; pointer-events: none !important; }
body > * { position: relative; z-index: 2; }
</style>
"""
    html = html.replace("</head>", background_fix + "</head>")

    response = Response(html, mimetype="text/html")
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response


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
        return _render_nova_page()

    # HTML
    @app.route("/html")
    def html():
        return _render_nova_page()

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
