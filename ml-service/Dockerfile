FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt
COPY . .
# Pre-download the model so it doesn't download on every startup
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis')"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]