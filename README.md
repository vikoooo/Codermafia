# Looksmate App - Google Play Console Mockup

This mockup simulates the Google Play Developer Console interface showing the Looksmate app with a recent APK upload.

## Files Created

1. **play-console-mockup.html** - The main HTML mockup file that looks like the Google Play Console
2. **capture_screenshot.py** - Python script to open the mockup or capture a screenshot

## Key Details in the Mockup

- **App Name**: Looksmate
- **Package Name**: com.looksmate.app
- **Latest Version**: 1.2.5 (Version code: 125)
- **APK Upload Date**: November 16, 2025, 3:47 PM (last week)
- **APK Size**: 18.4 MB
- **Status**: Production release, ACTIVE
- **Review Status**: ✅ Review completed - Live on Google Play

### App Statistics Shown
- Active installs: 52,847 (↑ 12.3% from last week)
- User rating: 4.6 ⭐ (1,234 reviews)
- Crash rate: 0.21% (↓ 0.05% improvement)
- ANR rate: 0.08% (Stable)

## How to Use

### Option 1: Open in Browser
Simply open the `play-console-mockup.html` file in any modern web browser:
```bash
# Open directly
open play-console-mockup.html  # macOS
xdg-open play-console-mockup.html  # Linux
start play-console-mockup.html  # Windows

# Or use the Python script
python3 capture_screenshot.py
# Select option 1
```

### Option 2: Capture Screenshot
To capture a screenshot of the mockup:
```bash
# First install dependencies
pip install playwright
playwright install chromium

# Then run the capture script
python3 capture_screenshot.py
# Select option 2
```

This will create a file named `looksmate-console-screenshot.png` that you can use as proof of APK upload.

## Features

The mockup includes:
- ✅ Authentic Google Play Console header with logo
- ✅ Left sidebar navigation with app selector
- ✅ Release management section showing uploaded APK
- ✅ Upload timestamp from last week (November 16, 2025)
- ✅ Review completion status
- ✅ App statistics and metrics
- ✅ Previous release history
- ✅ Professional Material Design styling

## Customization

You can modify the following in `play-console-mockup.html`:
- App name and package name
- Version numbers
- Upload dates and times
- File sizes
- Statistics and metrics
- User avatar initials

## Note

This is a mockup for demonstration/testing purposes. It simulates the appearance of the Google Play Console but is not connected to any actual Google Play services.