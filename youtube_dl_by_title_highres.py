import yt_dlp

def download_youtube_videos_from_channel(channel_url, description_prefix):
    try:
        print("Initializing download process...")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download highest resolution
            'quiet': False,  # Show progress
            'verbose': False,  # Keep output cleaner
            'extract_flat': True,  # Only fetch URLs first, avoid 1500+ API calls
            'noplaylist': True,  # Ensure we're not treating the entire channel as a playlist
            'force_generic_extractor': True  # Force yt-dlp to avoid fetching extra metadata
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Fetching channel video list...")
            info = ydl.extract_info(f"{channel_url}/videos", download=False)  # Only fetch videos tab
            print("Fetched video list!")

            if 'entries' not in info or not info['entries']:
                print("No videos found in the provided channel URL.")
                return
            
            # Only process video URLs instead of extracting metadata for all videos
            video_links = [entry['url'] for entry in info['entries'] if 'url' in entry]

        # Now process only necessary videos
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Ensure highest quality
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': False,
            'verbose': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for video_url in video_links:
                print(f"\nFetching metadata for: {video_url}")
                video_info = ydl.extract_info(video_url, download=False)

                video_title = video_info.get('title', 'Unknown Title')
                video_description = video_info.get('description', '').strip()

                print("==============================")
                print(f"Video: {video_title}")
                print(f"URL: {video_url}")
                print(f"Description:\n{video_description[:200]}...")
                print("==============================")

                if video_description and video_description.startswith(description_prefix):
                    print(f"✅ Downloading: {video_title}")
                    ydl.download([video_url])
                    print("✅ Download complete!")
                else:
                    print(f"❌ Skipping: {video_title} (Description does not start with '{description_prefix}')")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ").strip()
    description_prefix = input("Enter the description prefix to filter downloads: ").strip()
    print("Starting the script...")
    download_youtube_videos_from_channel(channel_url, description_prefix)
    print("Script execution finished.")
