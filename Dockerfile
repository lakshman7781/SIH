# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
# Copy only the requirements.txt to cache the pip install layer
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 9292
