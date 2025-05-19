# Use official Python image as base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pip tools
RUN pip install --upgrade pip

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy FastAPI app code and env file
COPY ./src /app/src
COPY .env /app/.env

WORKDIR /app/src

# Expose port
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "main:backend_app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
