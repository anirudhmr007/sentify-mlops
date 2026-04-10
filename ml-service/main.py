from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load the AI Model
sentiment_model = pipeline("sentiment-analysis")

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(request: TextRequest):
    # Run the AI model on the input text
    result = sentiment_model(request.text)[0] 
    return {"text": request.text, "sentiment": result['label'], "confidence": result['score']}