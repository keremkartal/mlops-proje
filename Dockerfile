FROM python:3.11-slim

WORKDIR /app

# Gereken dosyaları kopyala
COPY requirements.txt data.csv ./

# Paketleri kur
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu ve template klasörünü kopyala
COPY *.py ./
COPY templates ./templates

# Modeli eğit
RUN python train.py

# Portu aç ve uygulamayı başlat
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
