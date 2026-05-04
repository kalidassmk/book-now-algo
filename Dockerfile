FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxml2-dev libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python -c "import nltk; nltk.download('punkt', quiet=True)" || true

RUN chown -R pwuser:pwuser /app
USER pwuser

CMD ["python", "main.py"]
