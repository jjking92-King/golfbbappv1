# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY templates/ ./templates/

# Expose port 8080 (Cloud Run default)
EXPOSE 8080

# Set environment variables
ENV FLASK_APP=app.py
ENV PORT=8080

# Run gunicorn (production WSGI server)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
