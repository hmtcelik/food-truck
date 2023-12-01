# Base image
FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy the entire project directory
COPY . /app

# Install project dependencies
RUN pip install -r requirements.txt

# Migrate migrations
RUN python manage.py migrate

# Load initial data
RUN python manage.py load_foods

# Expose port
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
