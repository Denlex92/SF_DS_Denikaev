from pathlib import Path
import argparse
import json
import sys

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


def load_model(model_path: Path = MODEL_PATH):
    try:
        model = joblib.load(model_path)
    except Exception as e:
        print(f"Ошибка загрузки модели из {model_path}: {e}", file=sys.stderr)
        sys.exit(1)
    return model


def load_input_json(json_path: str) -> dict:
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения JSON {json_path}: {e}", file=sys.stderr)
        sys.exit(1)
    if not isinstance(data, dict):
        print("Ожидается JSON-объект с полями одной сессии", file=sys.stderr)
        sys.exit(1)
    return data


def make_dataframe_from_dict(data: dict) -> pd.DataFrame:
    # Гарантируем наличие всех фич, отсутствующие заполняем Наном
    row = {}
    for col in ALL_FEATURES:
        row[col] = data.get(col, np.nan)
    df = pd.DataFrame([row], columns=ALL_FEATURES)
    return df


def main():
    parser = argparse.ArgumentParser(
        description="Predict conversion probability for one session"
    )
    parser.add_argument(
        "--model-path",
        type=str,
        default="model_histgb.pkl",
        help="Path to saved model (joblib)"
    )
    parser.add_argument(
        "--input-json",
        type=str,
        required=True,
        help="Path to JSON file with session features"
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help="Decision threshold for label (default: 0.5)"
    )

    args = parser.parse_args()

    model = load_model(args.model_path)
    data_dict = load_input_json(args.input_json)
    df = make_dataframe_from_dict(data_dict)

    # Предсказание
    proba = model.predict_proba(df)[:, 1][0]
    label = int(proba >= args.threshold)

    result = {
        "probability": float(proba),
        "threshold": args.threshold,
        "label": label
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()