# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
