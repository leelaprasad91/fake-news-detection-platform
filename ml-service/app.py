from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

p = Path(__file__).resolve().parent / "fake_news_model.joblib"
model = joblib.load(p) if p.exists() else None
app = FastAPI(title="Fake News Detection API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class NewsRequest(BaseModel):
    text: str = Field(min_length=1, max_length=20000)

@app.get("/")
def home():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict")
def predict(req: NewsRequest):
    if model is None:
        raise HTTPException(503, "Run python train_model.py to create the model.")
    text = req.text.strip()
    if not text:
        raise HTTPException(422, "Text cannot be empty.")
    label = int(model.predict([text])[0])
    score = float(max(model.predict_proba([text])[0])) * 100
    return {"prediction": "LIKELY REAL" if label == 1 else "LIKELY FAKE",
            "label": "real" if label == 1 else "fake",
            "confidence": round(score, 2),
            "disclaimer": "Experimental demo model; not a verified fact-check."}
