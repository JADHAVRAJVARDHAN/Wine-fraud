
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the port the application will run on
EXPOSE 5000

# Specify the command to run the application
CMD ["python", "apps.py"]
