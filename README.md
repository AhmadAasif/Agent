# AI Agent

A lightweight, web-based AI agent built with **Python, Flask, and JavaScript**. The current implementation provides a simple voice-driven interface for interacting with Gmail and YouTube, with Gemini-powered email generation.

> **Project status:** Early development / prototype. The repository currently focuses on Gmail and YouTube integrations and is designed to grow into a broader computer-control AI agent.

## Overview

The agent provides a browser-based interface where a user can speak a command and have the application route it to the appropriate capability.

### Current capabilities

- 🎙️ **Voice command input** using the browser's Speech Recognition API.
- ✉️ **AI-assisted email drafting** with the Gemini API.
- 📧 **Gmail compose integration** that opens a pre-filled Gmail compose window for review.
- ▶️ **YouTube playback** by searching YouTube and opening the matching video in an embedded playback URL.
- 🌐 **Flask web backend** with JSON endpoints for agent operations.
- 🔗 **CORS support** for browser-based client communication.
- ❤️ **Health endpoint** for basic service monitoring.

## Architecture

```text
Browser UI
   │
   ├── Speech Recognition
   │
   ▼
Flask Application
   │
   ├── /agent ──────────► Gmail command detection
   │                         │
   │                         ├── Email extraction
   │                         ├── Gemini email generation
   │                         └── Gmail compose URL
   │
   └── /youtube/play ───► YouTube search
                             │
                             └── Video playback URL
```

## Project Structure

```text
Agent/
├── app/
│   ├── __init__.py              # Flask application factory and agent routes
│   ├── gmail/
│   │   ├── __init__.py          # Gmail package exports
│   │   ├── gmail_gen.py          # Gemini-powered email generation
│   │   └── gmail_write.py        # Email command detection and Gmail URL creation
│   ├── youtube/
│   │   ├── __init__.py          # YouTube Flask blueprint and endpoint
│   │   └── player.py             # YouTube search and playback URL generation
│   └── templates/
│       └── index.html            # Browser interface and client-side command handling
├── requirements.txt              # Python dependencies
├── wsgi.py                       # WSGI entry point
└── README.md
```

## Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Voice input | Web Speech API / Speech Recognition |
| Generative AI | Google Gemini API |
| Email | Gmail compose URL integration |
| Video | YouTube search and playback |
| Production server | Gunicorn |
| Cross-origin requests | Flask-CORS |

## Requirements

- Python 3.x
- A modern browser with Speech Recognition support for voice input
- A Gemini API key for AI email generation
- Internet access for Gemini and YouTube functionality

The current `requirements.txt` contains Flask, Flask-CORS, and Gunicorn. The Gemini integration uses Python's standard-library HTTP and JSON modules, so a separate Gemini Python SDK is not required by the current implementation.

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/AhmadAasif/Agent.git
cd Agent
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Set the Gemini API key before starting the application.

### Windows Command Prompt

```cmd
set GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

The application also supports the optional `GEMINI_MODEL` environment variable. If it is not provided, the current code defaults to `gemini-3.6-flash`.

**Security:** Never commit API keys, `.env` files containing secrets, or other credentials to the repository.

## Running Locally

Start the Flask application with:

```bash
flask --app wsgi run
```

Then open the local address shown by Flask in a browser.

The application exposes the following main routes:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | Main web interface |
| `GET` | `/html` | Main HTML interface |
| `GET` | `/health` | Service health check |
| `POST` | `/agent` | Process supported agent commands, currently email-focused |
| `POST` | `/youtube/play` | Search for and prepare a YouTube video for playback |

### Health check

```bash
curl http://127.0.0.1:5000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "nova AI Agent"
}
```

> The health response currently contains the legacy service label `nova AI Agent`; this is an implementation detail and can be renamed as the project branding is finalized.

## Gmail Workflow

The Gmail workflow is intentionally designed to generate a draft rather than silently send an email.

1. The user gives a voice command containing an email-related instruction.
2. The browser sends the command to `POST /agent`.
3. The backend checks whether the command is an email command.
4. An email address is extracted when one is present.
5. Gemini converts the command into a concise professional email.
6. The UI displays the generated recipient, subject, and body for review or editing.
7. The user can open a pre-filled Gmail compose window.

Example command:

```text
Create an email for manager@example.com asking for leave tomorrow.
```

The Gemini prompt is configured to avoid inventing names, dates, prices, companies, attachments, or other facts that were not supplied by the user.

## YouTube Workflow

The YouTube workflow accepts commands such as:

```text
play believer
play music shape of you
```

The backend searches YouTube for the requested query, extracts a video ID from the returned page, and generates a playback URL. The browser then opens or reuses a YouTube window for playback.

## API Examples

### Process an email command

```bash
curl -X POST http://127.0.0.1:5000/agent \
  -H "Content-Type: application/json" \
  -d "{\"command\":\"create an email for manager@example.com asking for a meeting\"}"
```

### Play a YouTube search

```bash
curl -X POST http://127.0.0.1:5000/youtube/play \
  -H "Content-Type: application/json" \
  -d "{\"command\":\"play believer\"}"
```

## Design Principles

- **Human-in-the-loop:** generated emails are presented for review before opening Gmail.
- **Modular architecture:** Gmail and YouTube functionality are separated into dedicated modules and a Flask blueprint.
- **Simple interfaces:** browser-to-backend communication uses lightweight JSON endpoints.
- **Extensibility:** the command-processing architecture is intended to support additional agent capabilities over time.
- **Graceful failure:** external API and search failures are returned as structured error responses where possible.

## Current Limitations

This repository represents an early version of the agent. The current code does **not** yet provide full Windows computer control, autonomous task planning, offline LLM support, text-input UI, or custom voice output.

The current browser interface is primarily voice-driven, and browser Speech Recognition availability depends on the browser and platform. Gemini-based email generation requires an API key and network access. YouTube search also requires network access.

## Roadmap

Planned development areas include:

- 🖥️ Windows desktop and computer-control capabilities
- 💬 Typed text input alongside voice input
- 🔊 Text-to-speech responses
- 🧠 Online + offline LLM support, including Gemini and a local model runtime such as Ollama
- 🤖 More autonomous command understanding and task execution
- 🌐 Broader web and application integrations
- 📦 Packaging the agent as an installable Windows application
- 🔐 Stronger secret management and production security
- 🧪 Automated testing and improved error handling

## Contributing

The project is under active development. Contributions, ideas, bug reports, and improvements are welcome as the architecture evolves.

Before submitting changes:

1. Keep features modular and focused.
2. Avoid committing secrets or machine-specific configuration.
3. Update the documentation when behavior or setup requirements change.
4. Test the affected endpoints and UI workflow locally.

## License

No open-source license has been specified for this repository yet. Until a license is added, the repository should not be assumed to grant permission to reuse, modify, or redistribute the code.

## Author

**Ahmad Aasif**

GitHub: https://github.com/AhmadAasif
