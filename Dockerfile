# Use a stable, lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (caching optimization)
COPY requirements.txt .

# Install dependencies (no-cache ensures clean builds)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose 8080 (useful only if using SSE mode)
EXPOSE 8080

# Default command to start the MCP server (stdio mode)
CMD ["python", "server.py"]