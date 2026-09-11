# Nova AI

Nova AI is a personal AI agent project built to make everyday computer tasks easier through natural language and voice commands.

The project is currently in its early development stage. Right now, Nova can handle basic Gmail and YouTube tasks through a simple browser interface. The long-term goal is to turn Nova into a practical Windows assistant that can understand what the user wants and carry out tasks on the computer with as little manual interaction as possible.

## What Nova Can Do

The current version focuses on two useful integrations:

- **Voice commands** — Nova accepts spoken commands through the browser's Speech Recognition API.
- **Gmail assistance** — Nova can turn a user's request into a professional email using the Gemini API and open a pre-filled Gmail compose window for review.
- **YouTube control** — Nova can search for a requested song or video and open it for playback.
- **Web interface** — A lightweight Flask backend connects the browser interface with Nova's functionality.
- **Health check** — A simple endpoint is available to confirm that the backend is running.

Nova is deliberately being developed in small, practical steps rather than trying to build everything at once.

## How It Works

At the moment, the flow is straightforward:

```text
User
  │
  │ Voice command
  ▼
Browser Interface
  │
  ▼
Flask Backend
  │
  ├── Gmail command
  │     ├── Extract email address
  │     ├── Generate email with Gemini
  │     └── Open Gmail compose
  │
  └── YouTube command
        ├── Search YouTube
        └── Open the requested video
```

This structure keeps each feature separate, making it easier to add more capabilities as the project grows.

## Project Structure

```text
Agent/
├── app/
│   ├── __init__.py              # Flask application and routes
│   ├── gmail/
│   │   ├── __init__.py          # Gmail package
│   │   ├── gmail_gen.py          # Gemini email generation
│   │   └── gmail_write.py        # Email command handling
│   ├── youtube/
│   │   ├── __init__.py          # YouTube route
│   │   └── player.py             # YouTube search and playback
│   └── templates/
│       └── index.html            # Nova's browser interface
├── requirements.txt
├── wsgi.py
└── README.md
```

## Technology

- Python
- Flask
- HTML, CSS and JavaScript
- Web Speech API
- Google Gemini API
- Gmail compose integration
- YouTube
- Flask-CORS
- Gunicorn

The current Gemini integration uses Python's built-in HTTP and JSON modules, so the Google Gemini Python SDK is not required.

## Getting Started

### Requirements

Before running Nova, make sure you have:

- Python 3.x installed
- A modern browser with Speech Recognition support
- A Gemini API key
- An internet connection for Gemini and YouTube features

### 1. Clone the repository

```bash
git clone https://github.com/AhmadAasif/Agent.git
cd Agent
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Command Prompt:

```cmd
set GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

You can also set `GEMINI_MODEL` if you want to use a different supported Gemini model. If it is not set, the current implementation uses `gemini-3.6-flash`.

**Do not commit your API key or other secrets to GitHub.**

### 5. Start Nova

```bash
flask --app wsgi run
```

Open the local address shown in the terminal to use the interface.

## Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Opens the Nova web interface |
| `GET` | `/html` | Opens the main HTML interface |
| `GET` | `/health` | Checks whether the backend is running |
| `POST` | `/agent` | Processes supported agent commands, currently focused on email |
| `POST` | `/youtube/play` | Searches for and prepares a YouTube video |

### Health Check

```bash
curl http://127.0.0.1:5000/health
```

## Gmail

Nova currently treats email generation as a review-first process rather than automatically sending messages.

For example, a command such as:

```text
Create an email for manager@example.com asking for leave tomorrow.
```

is sent to the backend. Nova identifies it as an email request, extracts the recipient, asks Gemini to prepare the message, and displays the result in the interface. The user can review or edit the message before opening it in Gmail.

The email generation prompt also tells Gemini not to make up information that was not provided by the user.

## YouTube

Nova can also handle simple YouTube commands, for example:

```text
play believer
play music shape of you
```

The backend searches YouTube for the requested content and prepares a playback URL. The browser then opens the video for the user.

## Current Limitations

Nova is still a work in progress. The current repository does not yet include the full Windows computer-control system planned for the project.

At this stage, Nova also does not yet have:

- Typed text input alongside voice input
- Text-to-speech responses
- Full Windows application and system control
- Offline/local LLM support
- Autonomous multi-step task execution
- A packaged Windows installer

These are planned parts of the project rather than features of the current release.

## Roadmap

The next stages of Nova's development are focused on making it more useful as a real desktop assistant:

1. Add Windows computer-control capabilities.
2. Add typed commands alongside voice input.
3. Add natural text-to-speech responses.
4. Support both online AI through Gemini and offline AI through a local model runtime such as Ollama.
5. Improve command understanding and multi-step task execution.
6. Add more web and application integrations.
7. Package Nova as an installable Windows application.
8. Improve security, testing, reliability and error handling.

The roadmap may evolve as new features are tested and the project grows.

## Development Approach

Nova is being built as a hands-on project, with each capability added and tested individually. The aim is to keep the code understandable and modular while gradually moving from a simple browser assistant toward a more capable Windows AI agent.

The project is intentionally open to improvements in architecture, AI models, voice technology and computer-control methods as development continues.

## Contributing

Nova is an active development project. Suggestions, bug reports and improvements are welcome.

When contributing, please:

1. Keep new functionality separated into sensible modules.
2. Do not commit API keys or other private information.
3. Update the README when setup or behavior changes.
4. Test the affected functionality before submitting changes.

## License

No open-source license has been added to this repository yet. Until a license is provided, the code should not be assumed to be available for unrestricted reuse or redistribution.

## Author

**Ahmad Aasif**

GitHub: https://github.com/AhmadAasif
