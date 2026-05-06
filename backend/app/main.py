from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from predict import predict_news


app = FastAPI(
    title="Fake News Detection API",
    description="Machine Learning API for detecting fake and true news.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NewsRequest(BaseModel):
    news: str


@app.get("/")
def home():
    return {
        "message": "Fake News Detection API is running successfully."
    }


@app.post("/predict")
def predict(request: NewsRequest):
    if not request.news.strip():
        return {
            "error": "Please enter news text."
        }

    result = predict_news(request.news)
    return result