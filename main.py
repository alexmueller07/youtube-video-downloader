import yt_dlp
import sys
import os
# https://www.youtube.com/watch?v=jyLXcy5SGd8
# https://www.youtube.com/watch?v=iHlyXfFLQgA

print("This program will download a youtube video as a MP4 file")

user_input = input("Enter the links to youtube videos you wish to download separated by a comma: ")
try:
    links = user_input.split(",")
    ydl_opts = {
        "quiet": True,
        "format": "best",
        "no_warnings": True,
        "outtmpl": "%(title)s.%(ext)s"
    }
    # Redirect stderr to suppress yt_dlp error output
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(links)
        finally:
            sys.stderr = old_stderr

except Exception as e:
    print("Failed downloading the video. Please make sure you enter a valid youtube video URL")