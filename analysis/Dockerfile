# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed dependencies specified in requirements.txt
RUN apt-get update && apt-get install -y \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir flask pandas pymongo matplotlib nltk wordcloud

# Expose port 5000 to the outside world
EXPOSE 9000

# Run app.py when the container launches
CMD ["python", "server.py"]
