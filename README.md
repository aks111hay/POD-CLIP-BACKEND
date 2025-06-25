# 🎙️ POD-CLIP Backend

POD-CLIP is an AI-powered podcast/video clip summarizer that extracts short segments from YouTube or uploaded videos and returns concise summaries using Google's Gemini API.

This is the **backend** service built using **FastAPI**. It supports:
- Downloading YouTube video clips via URL and timestamps
- Uploading local audio/video files
- Transcribing audio using OpenAI Whisper
- Summarizing with Gemini 2.5
- Storing summaries in a PostgreSQL database

---

## Swagger UI Demo 
![Swagger UI Screenshot](./Screenshot 2025-06-25 121402.png)

## POSTGRES DATABASE OUTPUT  
![pgadmin Screenshot](./Screenshot 2025-06-25 111733.png)

## 🚀 Features

- ⏬ Download YouTube clips by specifying timestamps
- 📁 Upload local audio/video files
- 📝 Auto transcription using Whisper
- 🤖 Summarization using Gemini API
- 🧠 Summary persistence with PostgreSQL
- 🔐 CORS enabled for frontend integration

---

## 🛠️ Tech Stack

- **FastAPI** – Python Web API framework
- **SQLAlchemy** – ORM with PostgreSQL
- **Google Gemini API** – for summarization
- **FFmpeg** – for clipping and audio processing
- **OpenAI Whisper** – for transcription
- **Uvicorn** – ASGI server for running FastAPI

---

## 📦 Project Structure
```
pod-clip/
├── app/
│ ├── api/
│ │ └── routes.py # API endpoints
│ ├── services/
│ │ ├── clipper.py # Save uploaded files
│ │ ├── youtube_dl.py # YouTube clip downloader
│ │ ├── transcription.py # Whisper-based transcription
│ │ └── gemini_client.py # Gemini summarization
│ ├── db/
│ │ ├── models.py # SQLAlchemy models
│ │ └── database.py # DB connection/session
│ └── config.py # Loads .env variables
├── media/ # Downloaded clips
├── requirements.txt
├── main.py # FastAPI app entrypoint
└── .env # Environment config
```


---

## 🧪 API Endpoints

| Method | Endpoint      | Description                   |
|--------|---------------|-------------------------------|
| POST   | `/upload`     | Upload local file or YouTube URL with start/end time |
| POST   | `/summarize`  | Transcribes + summarizes and stores in DB |

### Example `curl`:
```bash
curl -X POST http://127.0.0.1:8000/upload \
  -F "youtube_url=https://youtube.com/watch?v=abc123" \
  -F "start_time=00:00" \
  -F "end_time=00:45"
```
## Local setup
```
git clone https://github.com/aks111hay/POD-CLIP-BACKEND.git
cd pod-clip-backend
```
## Create Virtual Environment
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
## Install Requirements
```
pip install -r requirements.txt
```
## Create a .env file

- GEMINI_API_KEY=your_gemini_api_key
- DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/podclipdb

## Database Setup
```
# Create the database manually or via a client in pgadmin4
# Then run:
python
>>> from app.db.database import engine
>>> from app.db.models import Base
>>> Base.metadata.create_all(bind=engine)
```


## Run the Server
```
uvicorn main:app --reload
```

## Access the Swagger Docs
```
http://127.0.0.1:8000/docs
```
## Important Requirements
- Python 3.9+
- FFmpeg installed and added to PATH
- PostgreSQL running locally or remotely

