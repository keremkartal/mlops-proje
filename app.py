import logging
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
import joblib

# Logging yapılandırması
logging.basicConfig(
    level=logging.INFO,                             
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler("app.log"),            
        logging.StreamHandler()                   
    ]
)

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

@app.get("/")
def redirect_to_form():
    logging.info("Anasayfaya istek geldi, form sayfasına yönlendiriliyor.")
    return RedirectResponse(url="/form")

@app.post("/predict")
def predict(features: Features):
    data = [[features.TV, features.Radio, features.Newspaper]]
    prediction = model.predict(data)
    logging.info(f"JSON tahmin isteği: input: {data}, tahmin: {prediction[0]}")
    return {"prediction": float(prediction[0])}

# HTML formunu gösteren endpoint
@app.get("/form", response_class=HTMLResponse)
def form_page(request: Request):
    logging.info("Form sayfası görüntülendi.")
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
    logging.info(f"Formdan gelen veri: {data}, tahmin: {prediction[0]}")
    return templates.TemplateResponse("form.html", {
        "request": request,
        "prediction": round(float(prediction[0]), 2)
    })
