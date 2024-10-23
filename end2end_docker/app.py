from fastapi import FastAPI
from transformers import pipeline

# Load the sentiment analysis pipeline from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

# Initialize FastAPI app
app = FastAPI()

# Define a GET route for sentiment analysis
@app.get("/analyze")
def analyze(input_string: str):
    sentiment = sentiment_pipeline(input_string)
    return {
        "result": {
            "sentiment": sentiment[0]["label"],
            "score": sentiment[0]["score"]
        }
    }
