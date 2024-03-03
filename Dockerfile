# Use the official Python image from the Docker Hub
FROM python:3.12.2

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Use uvicorn to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]