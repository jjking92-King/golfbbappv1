FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

ENV PORT=8080
EXPOSE 8080

# Use gunicorn for production
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080", "--workers", "2"]
