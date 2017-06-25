# Use an image as a base image
FROM ubuntu:trusty

# Set the working directory to /doris
WORKDIR /doris

# Copy the current directory contents into the container at /doris
ADD . /doris

# Install any needed packages sepecified in requirements.txt
# RUN pip install -r requirements.txt

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Define environment variable
ENV NAME doris

# Run app.py when the container launches
# CMD ["python", "app.py"]
