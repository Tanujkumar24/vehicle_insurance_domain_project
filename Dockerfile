FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies required for ML & FastAPI packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for docker cache efficiency)
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy FULL project (IMPORTANT: includes templates folder)
COPY . .

# Expose FastAPI port
EXPOSE 5000

# Start FastAPI using uvicorn (production standard)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
