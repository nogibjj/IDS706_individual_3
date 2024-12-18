# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Set the environment variable for Flask
ENV GROQ_API_KEY=${GROQ_API_KEY}

# Run the application
CMD ["python", "app.py"]
