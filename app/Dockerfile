# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir flask requests pymongo

# Expose port 80 to allow communication to/from the container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
