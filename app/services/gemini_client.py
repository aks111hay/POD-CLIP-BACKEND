import google.generativeai as genai
from app.config import GEMINI_API_KEY

# Configure the API
genai.configure(api_key=GEMINI_API_KEY)

# Load the model (adjust model name if needed)
model = genai.GenerativeModel("gemini-2.5-flash")  # or "gemini-1.5-pro", etc.

def run_gemini_summary(transcript: str) -> str:
    prompt = f"Summarize the following podcast/audio transcript:\n\n{transcript}"
    response = model.generate_content(prompt)
    return response.text
