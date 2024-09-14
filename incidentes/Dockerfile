# Stage 1: Build the app
FROM python:3.9-slim AS builder

WORKDIR /app

# Copy only the necessary files for building dependencies
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.9-slim AS production

WORKDIR /app

# Copy the application files
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . /app

# Expose the port
EXPOSE 80

# Environment variables
ENV MODULE_NAME=app.main

# Start the application
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "3001", "main:app"]
