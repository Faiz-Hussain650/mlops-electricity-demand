from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd

app = FastAPI()

# Load latest MLflow model
model = mlflow.pyfunc.load_model("runs:/<replace_with_run_id>/model")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"prediction": float(prediction)}
