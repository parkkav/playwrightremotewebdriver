# Playwright Remote Driver Demo

This project demonstrates how to set up a Remote WebDriver using Playwright. It allows you to run a Playwright server on one machine and control it via a client script from another machine (or the same one).

## 🚀 Features

- **Remote Execution**: Run browser automation on a separate server.
- **WebSocket Communication**: Connects client and server via standard WebSockets.
- **Configurable**: Easy configuration via `config.json`.
- **Simple Example**: Includes a basic client that navigates to a site and takes a screenshot.

## 📋 Prerequisites

- Python 3.7+
- pip (Python package manager)

## 🛠️ Installation

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Playwright browsers** (required on the server machine):
    ```bash
    playwright install chromium
    ```

## ⚙️ Configuration

The server configuration is located in `config.json`:

```json
{
    "port": 9222,
    "wsPath": "playwright"
}
```

- `port`: The port the server will listen on.
- `wsPath`: The URL path for the WebSocket connection.

## 🏃 Usage

### 1. Start the Server

On the machine where you want the browser to run:

```bash
python server.py
```

The server will start and print the WebSocket endpoint, for example:
`ws://localhost:9222/playwright`

### 2. Run the Client

On the machine where you want to control the automation:

**Default (localhost):**
```bash
python client.py
```

**Custom Endpoint (Remote Machine):**
If your server is on a different machine, pass the WebSocket URL as an argument:

```bash
python client.py ws://<SERVER_IP>:9222/playwright
```

The client will:
1.  Connect to the remote browser.
2.  Navigate to `https://x.com`.
3.  Print the page title.
4.  Save a screenshot as `remote_screenshot.png`.

## 📂 Project Structure

- `server.py`: Launches the Playwright server and exposes the WebSocket endpoint.
- `client.py`: Connects to the server and performs automation tasks.
- `config.json`: Configuration file for the server.
- `requirements.txt`: Python dependencies.
- `medium_article.md`: A detailed guide on how this setup works.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
