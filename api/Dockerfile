# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install requests requests_oauthlib flask

EXPOSE 3000

# Run tweet.py when the container launches
CMD ["python", "tweet.py"]
