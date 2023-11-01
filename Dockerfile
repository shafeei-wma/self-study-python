# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHON_ENV=test

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . /app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the command to start uVicorn server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]