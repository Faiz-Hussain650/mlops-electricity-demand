import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.xgboost

# Load dataset (example: electricity demand CSV)
df = pd.read_csv("data/electricity.csv")
X = df.drop("demand", axis=1)
y = df["demand"]

# Split train/test
train_size = int(0.8 * len(df))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Start MLflow run
mlflow.set_experiment("Electricity-Demand-Forecast")

with mlflow.start_run():
    model = xgb.XGBRegressor(
        n_estimators=200, learning_rate=0.05, max_depth=6, random_state=42
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    # Log params, metrics, and model
    mlflow.log_params(model.get_params())
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)
    mlflow.xgboost.log_model(model, "model")

    print(f"RMSE: {rmse}, R2: {r2}")
