FROM python:3.11-slim AS base

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.6.1 \
    PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y \
    gcc libpq-dev curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY /app/requirements.txt ./
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Default command (can be overridden in docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
