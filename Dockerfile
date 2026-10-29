# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# python:3.9 still ships ca-certificates 20250419, which trusts the compromised
# eMudhra intermediates. urllib3 uses that bundle. trixie-security 20250419+deb13u1
# removes them. certifi is not on this path.
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/*

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
