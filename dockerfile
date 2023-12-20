    # Use the official Python image from Docker Hub
    FROM python:3.9-slim
    
    # Set environment variables
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    
    # Set work directory
    WORKDIR /app
    
    # Install dependencies
    COPY requirements.txt /app/
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy project
    COPY . /app/
    
    # Run the application
    CMD ["gunicorn", "-w", "3", "-b", ":8001", "merightnow.wsgi:application"]
