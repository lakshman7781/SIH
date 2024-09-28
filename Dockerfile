#Python image
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

#directory /app    
COPY . /app

#port 9292
EXPOSE 9292

# Run the application
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 9292"]
