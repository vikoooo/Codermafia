#!/usr/bin/env python3
"""
Capture a screenshot of the Google Play Console mockup
"""
import os
from playwright.sync_api import sync_playwright

def capture_screenshot():
    """Capture the HTML mockup as a PNG image"""
    html_file = os.path.abspath("play-console-mockup.html")
    output_file = "looksmate-play-console.png"
    
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=True)
        
        # Create a context with a specific viewport size
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            device_scale_factor=1.0
        )
        
        page = context.new_page()
        
        print(f"Loading mockup from: {html_file}")
        page.goto(f"file://{html_file}")
        
        # Wait for the page to fully load
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)  # Extra wait for any animations
        
        print(f"Capturing screenshot as: {output_file}")
        # Capture full page screenshot
        page.screenshot(
            path=output_file,
            full_page=True,
            type='png'
        )
        
        browser.close()
        
        # Get file size
        file_size = os.path.getsize(output_file)
        print(f"✅ Screenshot saved successfully!")
        print(f"📸 File: {output_file}")
        print(f"📊 Size: {file_size:,} bytes")
        
        return output_file

if __name__ == "__main__":
    capture_screenshot()