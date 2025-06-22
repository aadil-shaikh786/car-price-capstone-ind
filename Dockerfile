# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Cloud Run port
EXPOSE 8080

# CMD must match: <filename-without-py>:<FastAPI instance name>
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
