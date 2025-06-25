import uuid
from pathlib import Path
from fastapi import UploadFile

MEDIA_DIR = Path("media")
MEDIA_DIR.mkdir(exist_ok=True)

async def save_uploaded_clip(file: UploadFile) -> str:
    ext = file.filename.split('.')[-1]
    new_name = f"{uuid.uuid4()}.{ext}"
    path = MEDIA_DIR / new_name

    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    return str(path)
