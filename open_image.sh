#!/bin/bash

echo "Opening Looksmate Play Console image..."

# Detect OS and use appropriate command
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open looksmate-play-console.png
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    xdg-open looksmate-play-console.png
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    # Windows
    start looksmate-play-console.png
else
    echo "Could not detect OS. Please open looksmate-play-console.png manually."
fi

echo ""
echo "If the image didn't open, try:"
echo "- Double-click on looksmate-play-console.png in File Explorer/Finder"
echo "- Or open play-console-mockup.html in your browser"