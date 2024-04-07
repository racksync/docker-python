# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory in the container to /app
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./
RUN pip install -r requirements.txt  # Install dependencies (if any)
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python3", "app.py"]