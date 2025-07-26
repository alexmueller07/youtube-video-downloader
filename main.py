import yt_dlp
import sys
import os

# Simple console app to download YouTube videos as MP4 using yt_dlp
print("This program will download a youtube video as a MP4 file")

# Prompt the user to enter one or more YouTube links
user_input = input("Enter the links to youtube videos you wish to download separated by a comma: ")

try:
    # Split input into a list of URLs
    links = user_input.split(",")

    # Set yt_dlp options
    ydl_opts = {
        "quiet": True,            # Suppress verbose output
        "format": "best",         # Download best quality video available
        "no_warnings": True,      # Don't show warnings
        "outtmpl": "%(title)s.%(ext)s"  # Save as the video's title with appropriate extension
    }

    # Redirect stderr to suppress non-critical yt_dlp errors/warnings
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            # Initialize and run the downloader
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(links)
        finally:
            # Restore stderr so it doesn’t affect future output
            sys.stderr = old_stderr

except Exception as e:
    # Basic error message if anything goes wrong (e.g., invalid link, network error)
    print("Failed downloading the video. Please make sure you enter a valid youtube video URL")
