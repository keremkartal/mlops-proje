FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt data.csv ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY *.py ./
COPY templates ./templates

RUN python train.py

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
