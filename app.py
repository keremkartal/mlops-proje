from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# FastAPI uygulamasını başlat
app = FastAPI()

# Eğitilmiş modeli yükle
model = joblib.load("model.pkl")

# Giriş verilerinin yapısını tanımla (feature isimlerine göre)
class Features(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

# Ana endpoint → Servisin aktif olup olmadığını kontrol eder
@app.get("/")
def read_root():
    return {"message": "Model hazır"}

# Tahmin endpoint'i → POST isteği ile çalışır
@app.post("/predict")
def predict(features: Features):
    # Modele uygun formatta feature'ları düzenle
    data = [[features.TV, features.Radio, features.Newspaper]]
    prediction = model.predict(data)
    return {"prediction": float(prediction[0])}

