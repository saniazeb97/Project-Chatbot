# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables to avoid Python buffering and to ensure proper locales
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . /app/

# Expose the ports for both FastAPI and Streamlit
# FastAPI typically runs on port 8000
EXPOSE 8000

# Streamlit typically runs on port 8501
EXPOSE 8501

# Set up a command to run both FastAPI and Streamlit apps using a process manager like "supervisord"
# Install "supervisord" to manage multiple processes
RUN apt-get update && apt-get install -y supervisor

# Create a supervisord configuration file to run FastAPI and Streamlit
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Run the supervisord process manager to start both apps
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
