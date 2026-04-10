from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# --- ADDED: CORS Middleware Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (safe for local testing)
    allow_credentials=True,
    allow_methods=["*"],  # This tells FastAPI to accept OPTIONS, POST, GET, etc.
    allow_headers=["*"],
)
# --------------------------------------------

# The URL of the ML service (will be set via environment variables in Docker/K8s)
ML_SERVICE_URL = os.getenv("ML_SERVICE_URL", "http://localhost:8000/analyze")

class UserInput(BaseModel):
    text: str

@app.post("/api/sentiment")
def get_sentiment(user_input: UserInput):
    try:
        # Forward the request to the ML Service
        response = requests.post(ML_SERVICE_URL, json={"text": user_input.text})
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail="ML Service is down.")