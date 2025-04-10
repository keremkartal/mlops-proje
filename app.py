from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
import joblib

# FastAPI uygulamasını başlat
app = FastAPI()

# Jinja2 templates klasörünü tanımla
templates = Jinja2Templates(directory="templates")

# Eğitilmiş modeli yükle
model = joblib.load("model.pkl")

# API üzerinden kullanılacak veri yapısı
class Features(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

# Ana endpoint → doğrudan form ekranına yönlendir
@app.get("/")
def redirect_to_form():
    return RedirectResponse(url="/form")

# API için JSON tabanlı tahmin (programatik kullanım için)
@app.post("/predict")
def predict(features: Features):
    data = [[features.TV, features.Radio, features.Newspaper]]
    prediction = model.predict(data)
    return {"prediction": float(prediction[0])}

# HTML formunu gösteren endpoint
@app.get("/form", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Formdan gelen veriyi işleyip sonucu HTML ile gösteren endpoint
@app.post("/predict-form", response_class=HTMLResponse)
def predict_form(
    request: Request,
    TV: float = Form(...),
    Radio: float = Form(...),
    Newspaper: float = Form(...)
):
    data = [[TV, Radio, Newspaper]]
    prediction = model.predict(data)
    return templates.TemplateResponse("form.html", {
        "request": request,
        "prediction": round(float(prediction[0]), 2)
    })
