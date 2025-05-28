# Satış Tahmini için Uçtan Uca MLOps Projesi

##  Proje Açıklaması
Reklam harcamalarına dayalı satış tahmini yapan Lineer Regresyon modelinin MLOps yaşam döngüsünü kapsar. Model eğitimi, versiyonlama, deney takibi, API entegrasyonu, containerizasyon ve CI/CD süreçleri içerir.

##  Temel Özellikler
* **Otomatik Pipeline**: DVC ile tekrarlanabilir model eğitimi (`dvc repro`)
* **Deney Takibi**: MLflow ile parametre/metrik kaydı (RMSE)
* **Versiyon Kontrol**: Git (kod+veri) + DVC (model)
* **Dağıtım**: FastAPI ile REST API + Docker konteyner
* **CI/CD**: GitHub Actions ile otomatik yeniden eğitim ve Docker build

##  Kullanılan Teknolojiler
* **Dil**: Python 3.11
* **ML**: Scikit-learn, Pandas, MLflow
* **API**: FastAPI, Uvicorn
* **DevOps**: DVC, Docker, GitHub Actions

##  Kurulum
### Gereksinimler
- Git
- Python 3.9+
- Docker Desktop

```bash
# 1. Repoyu klonla
git clonehttps://github.com/keremkartal/mlops-proje.git
cd mlops-proje

# 2. Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

## ⚙️ Kullanım
### Model Eğitimi
```bash
dvc repro  # Pipeline'ı çalıştırır
```

### Deney Takibi
```bash
mlflow ui --host 0.0.0.0 --port 5000
```
http://localhost:5000 adresinden erişim

### API Başlatma
```bash
uvicorn app:app --reload --port 8000
```
- **Web Form**: `http://localhost:8000/form`
- **Swagger Docs**: `http://localhost:8000/docs`

### Docker ile Çalıştırma
```bash
docker build -t satis-tahmin .
docker run -p 8000:8000 satis-tahmin
```

##  API Endpoints
- `POST /predict`: JSON input ile tahmin
  ```json
  {"TV": 230.1, "Radio": 37.8, "Newspaper": 69.2}
  ```
- `GET /form`: HTML tahmin formu
- `POST /predict-form`: Form input ile tahmin

##  CI/CD Otomasyonu
`.github/workflows/ci.yaml` dosyası ile:
- Her push'da otomatik model yeniden eğitimi
- Docker imaj build otomasyonu
- MLflow deney takibi entegrasyonu
