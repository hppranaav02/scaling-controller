#!/bin/bash
# Default values for the flags
s_value=""
d_value=""

# Parse args
while getopts ":s:f:d:" opt; do
  case ${opt} in
    s)
      s_value=${OPTARG}
      ;;
    d)
      d_value=${OPTARG}
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

# Create the webapp container image
cd /webapp
podman build -t webapp .
cd ..

# Run the first webapp container
if [ $d_value -ne "" ]
then
  podman run -d -p 5000:80 -v $d_value:/app/data webapp1
else
  podman run -d -p 5000:80 -v /home/data:/app/data webapp1

# Run a quick test on the GET / API


# Create the nginx image
cd /nginx
podman build -t nginx .
cd ..

# Run the nginx container
if [ $d_value -ne "" ]
then
  podman run -d 8086:80 -v $d_value:/conf/data nginx
else
  podman run -d 8086:80 -v /home/nconf:/nconf/data nginx
fi

# Run the scaling controller (On default scaling algorithm)
python3 scaler.py

# If -s flag == 'single', Run the locust engine for single container load test else run full expiremnt
if [ $s_value -eq "single" ]
then
  # run locust single load test
else
  echo 
fi
