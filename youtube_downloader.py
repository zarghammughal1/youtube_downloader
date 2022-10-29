"""
    This will download the youtube video and then show the video downloaded successfully!.
    Libraries that should be installed.
        pip install pytube
"""
from pytube import YouTube
import os

# Function that download the youtube video.
def downloader(url):
    """
        It will download the youtube video.
    """
    yt_vid = YouTube(url).streams.filter(progressive=True)
    yt_vid.order_by('resolution').desc().first().download()
    print("Video Download Successfully!")


# Function Calling.
downloader("https://www.youtube.com/watch?v=-T9XExlPv1Y")
