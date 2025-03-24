FROM python:3.11-slim

WORKDIR /app

# Önce tüm statik dosyaları kopyala
COPY requirements.txt data.csv ./

# Bağımlılıkları kur
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY *.py ./

# Modeli eğit
RUN python train.py

# Port ve çalıştırma ayarları
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]