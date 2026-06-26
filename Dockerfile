# Use an official Python runtime as a parent image (slim reduces image size)
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Render exposes the PORT environment variable (defaults to 10000)
EXPOSE 10000

# Command to run the application using Gunicorn (recommended for production)
# This assumes your Flask app object is named 'app' inside 'app.py'
CMD gunicorn app:app --bind 0.0.0.0:${PORT:-10000}