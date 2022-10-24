# Proofreading Tool
# pip install pytube
from pytube import YouTube
import os

def downloader(url):
    yt_vid = YouTube(url).streams.filter(progressive=True)
    yt_vid.order_by('resolution').desc().first().download()
    print("Video Download Successfully!")


url_Of_Video = "https://www.youtube.com/watch?v=-T9XExlPv1Y"
downloader(url_Of_Video)
