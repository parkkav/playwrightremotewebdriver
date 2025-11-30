import sys
from playwright.sync_api import sync_playwright

def run_client(ws_endpoint):
    print(f"Connecting to remote browser at: {ws_endpoint}")
    with sync_playwright() as p:
        # Connect to the remote browser
        browser = p.chromium.connect(ws_endpoint)
        
        # Create a new page
        page = browser.new_page()
        
        print("Navigating to example.com...")
        page.goto("https://x.com")
        
        title = page.title()
        print(f"Page title: {title}")
        
        screenshot_path = "remote_screenshot.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
        
        # Close the browser connection (does not stop the server)
        browser.close()

if __name__ == "__main__":
    ws_endpoint = "ws://localhost:9222/playwright"
    if len(sys.argv) > 1:
        ws_endpoint = sys.argv[1]
    
    run_client(ws_endpoint)
