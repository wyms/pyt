import os
import subprocess
import sys
from moviepy.editor import VideoFileClip
from datetime import timedelta

def get_video_duration(path):
    try:
        clip = VideoFileClip(path)
        duration = clip.duration  # in seconds (float)
        clip.close()
        return duration
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return 0

def format_time(seconds):
    return str(timedelta(seconds=int(seconds)))  # e.g., 0:02:35

def main():
    folder = r"C:\ingram_movies"
    print(f"🔍 Looking for MP4 files in: {folder}")
    
    mp4_files = [f for f in os.listdir(folder) if f.lower().endswith('.mp4')]
    mp4_files.sort()

    if not mp4_files:
        print("❌ No MP4 files found in the folder.")
        sys.exit(1)

    print(f"✅ Found {len(mp4_files)} MP4 files.")

    list_file_path = os.path.join(folder, "file_list.txt")
    description_path = os.path.join(folder, "youtube_description.txt")
    output_file = os.path.join(folder, "output.mp4")

    cumulative_time = 0
    chapter_lines = []

    with open(list_file_path, "w", encoding="utf-8") as list_file:
        for i, filename in enumerate(mp4_files, start=1):
            full_path = os.path.join(folder, filename)

            # Convert path to ffmpeg-friendly format (forward slashes, escaped single quotes)
            safe_path = full_path.replace("\\", "/").replace("'", "'\\''")
            list_file.write(f"file '{safe_path}'\n")

            print(f"📹 Processing: {filename}")
            duration = get_video_duration(full_path)
            timestamp = format_time(cumulative_time)
            title = os.path.splitext(filename)[0]
            chapter_lines.append(f"{timestamp} – {i:02d}. {title}")
            cumulative_time += duration

    # Write YouTube description
    with open(description_path, "w", encoding="utf-8") as desc_file:
        desc_file.write("Ingram Family Home Movies Compilation (1939–1960)\n\n")
        desc_file.write("This compilation features historic and heartwarming home movies from the Ingram family archives, spanning over two decades of family milestones, travel, and everyday life.\n\n")
        desc_file.write("**Chapters:**\n")
        for line in chapter_lines:
            desc_file.write(line + "\n")

    print("📄 Description file written to:", description_path)

    # Combine video files using ffmpeg
    print("🛠️ Combining videos using ffmpeg...")
    cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file_path,
        "-c", "copy",
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print("✅ Successfully concatenated videos into:", output_file)
    except subprocess.CalledProcessError as e:
        print("❌ Error during concatenation:", e)

    os.remove(list_file_path)
    print("🧹 Cleaned up temporary files.")

if __name__ == "__main__":
    main()
