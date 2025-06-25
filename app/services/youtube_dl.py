import os
import subprocess
from datetime import datetime
from pathlib import Path
import uuid

MEDIA_DIR = Path("media")
MEDIA_DIR.mkdir(exist_ok=True)

async def download_youtube_clip(url: str, start: str, end: str) -> str:
    filename = f"{uuid.uuid4()}.mp4"
    full_path = MEDIA_DIR / filename
    temp_path = MEDIA_DIR / f"full_{filename}"

    # Download full audio using yt-dlp
    subprocess.run(["yt-dlp", "-f", "bestaudio", "-o", str(temp_path), url])

    # Clip the audio using ffmpeg
    subprocess.run([
        "ffmpeg",
        "-i", str(temp_path),
        "-ss", start,
        "-to", end,
        "-c", "copy",
        str(full_path)
    ])
    temp_path.unlink(missing_ok=True)
    return str(full_path)
