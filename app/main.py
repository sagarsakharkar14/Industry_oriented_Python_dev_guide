# app/main.py
import os

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model.joblib")
app = FastAPI(title="Simple ML microservice")


class PredictRequest(BaseModel):
    features: list


try:
    model = joblib.load(os.path.abspath(MODEL_PATH))
except Exception:
    model = None


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict")
def predict(req: PredictRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    arr = np.array(req.features).reshape(1, -1)
    pred = model.predict(arr)[0]
    proba = model.predict_proba(arr)[0].tolist()
    return {"prediction": int(pred), "probability": proba}
