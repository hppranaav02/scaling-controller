# Using slim-buster to improve compatibility over alpines reduced footprint
FROM python:3.8-slim-buster

# Create and add files to the working directory
WORKDIR /app

ADD . /app

RUN pip install bz2 pathlib time random flask

# Create a virtual environment and activate it
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Install Flask extensions
RUN pip install flask_limiter flask_restful

# Make port 80 available out of network
EXPOSE 80

# Run the webapp
CMD ["python", "objst.py"]
