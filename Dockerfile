FROM python:3.11-slim

WORKDIR /app



COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY train.py .  

# Model dosyasını oluşturmak için train.py'yi çalıştır
RUN python train.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]