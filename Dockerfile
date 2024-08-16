# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY myproject /app/myproject

# Set the environment variable for Python path
ENV PYTHONPATH=/app/myproject

# Specify the command to run on container start
CMD ["python", "/app/myproject/main.py"]
