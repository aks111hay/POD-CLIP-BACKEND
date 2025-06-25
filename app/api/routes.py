from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from app.services.youtube_dl import download_youtube_clip
from app.services.clipper import save_uploaded_clip

router = APIRouter()

@router.post("/upload")
async def upload_clip(
    file: Optional[UploadFile] = File(None),
    youtube_url: Optional[str] = Form(None),
    start_time: Optional[str] = Form(None),  # format: "00:01:20"
    end_time: Optional[str] = Form(None)
):
    if file:
        path = await save_uploaded_clip(file)
        return {"status": "uploaded", "path": path}

    elif youtube_url and start_time and end_time:
        path = await download_youtube_clip(youtube_url, start_time, end_time)
        return {"status": "downloaded", "path": path}

    return {"error": "Provide a file or YouTube URL + timestamps"}

from fastapi import Form
from app.services.gemini_client import run_gemini_summary

from app.services.transcription import transcribe_audio
from app.services.gemini_client import run_gemini_summary

from pydantic import BaseModel

class ClipRequest(BaseModel):
    path: str

# app/api/routes.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.services.gemini_client import run_gemini_summary
from app.db.database import SessionLocal
from app.db.models import Summary



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/summarize")
async def summarize_clip(data: ClipRequest, db: Session = Depends(get_db)):
    transcript = transcribe_audio(data.path)
    summary = run_gemini_summary(transcript)
    summary_entry = Summary(video_path=data.path, summary=summary)
    db.add(summary_entry)
    db.commit()
    db.refresh(summary_entry)
    return {"summary": summary, "id": summary_entry.id}