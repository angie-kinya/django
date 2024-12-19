# Use official Python image as a base
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED 1         # Prevent buffering of Python output

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Expose the port for Django
EXPOSE 8000

# Run migrations and start Django server
CMD ["gunicorn", "personal_blog.wsgi:application", "--bind", "0.0.0.0:8000"]
