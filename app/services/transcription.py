import whisper
import uuid
import os

model = whisper.load_model("base")

def transcribe_audio(mp4_path: str) -> str:
    audio_path = mp4_path.replace(".mp4", ".mp3")
    os.system(f"ffmpeg -i {mp4_path} -q:a 0 -map a {audio_path} -y")
    
    result = model.transcribe(audio_path)
    return result["text"]
