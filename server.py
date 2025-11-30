import subprocess
import sys
import re

def run_server():
    print("Starting Playwright Server via CLI...")
    # Launch the playwright server using the CLI
    # We use --headless false to see the browser
    cmd = ["playwright", "launch-server", "--browser", "chromium", "--config", "config.json"]
    
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    ws_endpoint = None
    
    try:
        # Read output line by line
        for line in iter(process.stdout.readline, ''):
            print(line, end='') # Echo output
            if not ws_endpoint and "ws://" in line:
                # Extract WS endpoint
                match = re.search(r'ws://\S+', line)
                if match:
                    ws_endpoint = match.group(0)
                    print(f"\nCaptured WS Endpoint: {ws_endpoint}")
                    print("You can now run the client script with this endpoint.")
                    
        process.wait()
    except KeyboardInterrupt:
        print("\nStopping server...")
        process.terminate()
        process.wait()

if __name__ == "__main__":
    run_server()
