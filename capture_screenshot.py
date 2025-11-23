#!/usr/bin/env python3
"""
Script to open the Google Play Console mockup in a browser or capture a screenshot.
You can use this to view or save the mockup as an image.
"""

import os
import sys
import webbrowser
import subprocess
import time

def open_in_browser():
    """Open the HTML file in the default web browser"""
    html_file = os.path.abspath("play-console-mockup.html")
    
    if not os.path.exists(html_file):
        print("Error: play-console-mockup.html not found!")
        return False
    
    print(f"Opening mockup in browser: {html_file}")
    webbrowser.open(f"file://{html_file}")
    return True

def capture_with_playwright():
    """Capture screenshot using Playwright (requires installation)"""
    try:
        from playwright.sync_api import sync_playwright
        
        html_file = os.path.abspath("play-console-mockup.html")
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': 1920, 'height': 1080})
            page.goto(f"file://{html_file}")
            
            # Wait for content to load
            time.sleep(2)
            
            # Take screenshot
            screenshot_path = "looksmate-console-screenshot.png"
            page.screenshot(path=screenshot_path, full_page=True)
            browser.close()
            
            print(f"Screenshot saved as: {screenshot_path}")
            return True
            
    except ImportError:
        print("Playwright not installed. Install with: pip install playwright")
        print("Then run: playwright install chromium")
        return False
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return False

def install_dependencies():
    """Install required dependencies for screenshot capture"""
    print("Installing dependencies for screenshot capture...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
        subprocess.run(["playwright", "install", "chromium"], check=True)
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        return False

def main():
    print("Google Play Console Mockup - Looksmate App")
    print("=" * 50)
    print("\nThis mockup shows the Looksmate app with:")
    print("- APK version 1.2.5 uploaded on November 16, 2025")
    print("- Production release status: ACTIVE")
    print("- 52,847 active installs")
    print("- 4.6 star rating")
    print("\nOptions:")
    print("1. Open in browser (default)")
    print("2. Capture screenshot (requires Playwright)")
    print("3. Install dependencies for screenshot")
    
    choice = input("\nSelect option (1/2/3) [default: 1]: ").strip() or "1"
    
    if choice == "1":
        open_in_browser()
    elif choice == "2":
        if not capture_with_playwright():
            print("\nWould you like to install the dependencies? (y/n)")
            if input().lower() == 'y':
                if install_dependencies():
                    capture_with_playwright()
    elif choice == "3":
        install_dependencies()
    else:
        print("Invalid option. Opening in browser...")
        open_in_browser()

if __name__ == "__main__":
    main()