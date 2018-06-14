# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./install-auth.sh /app

# Install any needed packages specified in requirements.txt
RUN /app/install-auth.sh --quiet

# Make port 80 available to the world outside this container
#EXPOSE 5000

# Define environment variable
ENV NAME World


# Run app.py when the container launches
ENTRYPOINT ["/app/resmon-auth", "--port 5000"]

