from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "models" / "model_histgb.pkl"

NUM_FEATURES = ["hits_count", "unique_pages", "events_count", "visit_number"]
CAT_FEATURES = [
    "utm_source", "utm_medium", "utm_campaign", "utm_adcontent", "utm_keyword",
    "device_category", "device_os", "device_brand", "device_browser",
    "geo_country", "geo_city"
]
ALL_FEATURES = NUM_FEATURES + CAT_FEATURES
DEFAULT_THRESHOLD = 0.5

app = FastAPI(
    title="SberAuto Subscription Conversion API",
    description="API for predicting session conversion probability",
    version="1.0.0"
)

try:
    model = joblib.load(MODEL_PATH)
    model_load_error = None
except Exception as e:
    model = None
    model_load_error = str(e)


class SessionFeatures(BaseModel):
    hits_count: float = Field(..., ge=0)
    unique_pages: float = Field(..., ge=0)
    events_count: float = Field(..., ge=0)
    visit_number: float = Field(..., ge=0)

    utm_source: str | None = None
    utm_medium: str | None = None
    utm_campaign: str | None = None
    utm_adcontent: str | None = None
    utm_keyword: str | None = None

    device_category: str | None = None
    device_os: str | None = None
    device_brand: str | None = None
    device_browser: str | None = None

    geo_country: str | None = None
    geo_city: str | None = None


class PredictionResponse(BaseModel):
    probability: float
    threshold: float
    label: int


def to_dataframe(payload: SessionFeatures) -> pd.DataFrame:
    data = payload.model_dump()
    row = {col: data.get(col, np.nan) for col in ALL_FEATURES}
    return pd.DataFrame([row], columns=ALL_FEATURES)


@app.get("/")
def root():
    return {
        "message": "Conversion prediction API is running",
        "docs": "/docs",
        "model_loaded": model is not None
    }


@app.get("/health")
def health():
    return {
        "status": "ok" if model is not None else "error",
        "model_loaded": model is not None,
        "model_path": MODEL_PATH,
        "error": model_load_error
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: SessionFeatures, threshold: float = DEFAULT_THRESHOLD):
    if model is None:
        raise HTTPException(
            status_code=500,
            detail=f"Model is not loaded: {model_load_error}"
        )

    if not 0 <= threshold <= 1:
        raise HTTPException(status_code=400, detail="threshold must be between 0 and 1")

    df = to_dataframe(payload)
    proba = float(model.predict_proba(df)[:, 1][0])
    label = int(proba >= threshold)

    return PredictionResponse(
        probability=proba,
        threshold=threshold,
        label=label
    )