import os
from pytube import YouTube

# Get the video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the video title
video_title = yt.title

# Download the video in the highest resolution
video = yt.streams.get_highest_resolution()

# Create a directory to save the video
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Download the video
video.download(output_path="downloads", filename=f"{video_title}.mp4")

print(f"Video downloaded successfully: {video_title}")