import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Test fonksiyonlarınız burada...
def test_read_root_redirect():
    response = client.get("/")
    assert response.status_code in (200, 307)

def test_form_page():
    response = client.get("/form")
    assert response.status_code == 200
    assert "form" in response.text.lower()

def test_predict_json():
    json_data = {"TV": 230.1, "Radio": 37.8, "Newspaper": 69.2}
    response = client.post("/predict", json=json_data)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data

def test_predict_form():
    form_data = {"TV": 230.1, "Radio": 37.8, "Newspaper": 69.2}
    response = client.post("/predict-form", data=form_data)
    assert response.status_code == 200
    assert "tahmin" in response.text.lower() or "prediction" in response.text.lower()

