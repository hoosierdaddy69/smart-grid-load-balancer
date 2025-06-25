FROM python:3.10-slim

WORKDIR /app
COPY main.py .

RUN pip install flask prometheus_client

CMD ["python", "main.py"]
# Dockerfile for substation service
