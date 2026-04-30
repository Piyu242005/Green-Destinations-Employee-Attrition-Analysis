# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create the models directory
RUN mkdir -p models

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Command to run both the FastAPI backend and Streamlit frontend
# In a real production setup, you'd use a process manager like supervisord
CMD uvicorn app.api:app --host 0.0.0.0 --port 8000 & streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0
