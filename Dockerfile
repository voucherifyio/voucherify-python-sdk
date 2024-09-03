# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements files first to leverage Docker caching
COPY requirements.txt test-requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r test-requirements.txt

# Set up a volume to store data
VOLUME /app/data

# Copy the rest of the application code
COPY . .

# Run the application
CMD ["python", "./__tests__/main.py"]
