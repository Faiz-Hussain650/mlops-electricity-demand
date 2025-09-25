from fastapi.testclient import TestClient
from ml.predict import app

client = TestClient(app)

def test_prediction():
    response = client.post("/predict", json={"datetime": "2006-12-16 17:24:00"})
    assert response.status_code == 200
    assert "prediction" in response.json()
