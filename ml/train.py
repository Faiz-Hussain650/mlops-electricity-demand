import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.xgboost

def load_and_preprocess(path="/Users/faizhussain/Desktop/mlops-electricity-demand/data/household_power.textClipping"):
    # Load .txt with semicolon separator
    df = pd.read_csv(path, sep=";", low_memory=False)

    # Combine Date + Time
    df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"],
                                    format="%d/%m/%Y %H:%M:%S",
                                    errors="coerce")

    # Replace '?' with NaN, drop missing
    df = df.replace("?", np.nan).dropna()

    # Convert numeric
    df["Global_active_power"] = df["Global_active_power"].astype(float)

    # Feature engineering
    df["hour"] = df["Datetime"].dt.hour
    df["dayofweek"] = df["Datetime"].dt.dayofweek
    df["month"] = df["Datetime"].dt.month

    return df

if __name__ == "__main__":
    df = load_and_preprocess("data/household_power.txt")

    X = df[["hour", "dayofweek", "month"]]
    y = df["Global_active_power"]

    train_size = int(0.8 * len(df))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    mlflow.set_experiment("Household-Power-Forecast")

    with mlflow.start_run():
        model = xgb.XGBRegressor(n_estimators=200, learning_rate=0.1)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))

        mlflow.log_params(model.get_params())
        mlflow.log_metric("rmse", rmse)
        mlflow.xgboost.log_model(model, "model")

        print("✅ Training complete | RMSE:", rmse)
