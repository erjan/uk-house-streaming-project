# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements_docker.txt

# Make the script executable
RUN chmod +x producer.py

# Run the script with the provided configuration file as an argument


CMD ["/usr/local/bin/python3.11", "producer.py"]

