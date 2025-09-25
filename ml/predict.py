from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd
from datetime import datetime

app = FastAPI()

# Load latest MLflow model (replace with your latest run ID)
model = mlflow.pyfunc.load_model("runs:/<your_run_id>/model")

@app.post("/predict")
def predict(data: dict):
    # Example input: {"datetime": "2006-12-16 17:24:00"}
    dt = pd.to_datetime(data["datetime"])
    features = pd.DataFrame([{
        "hour": dt.hour,
        "dayofweek": dt.dayofweek,
        "month": dt.month
    }])
    pred = model.predict(features)[0]
    return {"prediction": float(pred)}
