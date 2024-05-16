<!-- Getting started -->
# Getting started
This is an autoscalar for a web application running as a podman container. It is designed to automatically scale the number of contaienrs based on the number of requests to the application.

## Prerequisites
- Podman

## Web application
The web application is a simple Python Flask application that returns a JSON response with the multiple API endpoints. The application is running on port 5000.
<!-- List steps to run the webapp as a podman container -->
## Steps to run the webapp as a podman container
1. Clone the repository
2. Build the container image in the webapp directory with the following command
```podman build -t webapp .```
3. Run the container with the following command
```podman run -d -p 5000:5000 -v /Users/pradeep/Desktop/LeidenUni/sem2/CC/scaling-controller/webapp/data:/app/data --name webapp1 webapp```

## Load Balancer
We make use of a HAProxy load balancer to distribute the incoming requests to the web application containers. 

<!-- List steps to run the load balancer as a podman container -->
## Steps to run the load balancer as a podman container
1. Clone the repository
2. Go to the haproxy direcctory in the repository
3. Build the container image with the following command
```podman build -t haproxy .```
4. Run the container with the following command
```podman run -d --restart always --name haproxy -p 8080:8080 -p 9999:9999 -p 8888:8888 -v /Users/pradeep/Desktop/LeidenUni/sem2/CC/scaling-controller/haproxy/conf:/etc/haproxy  haproxy```

## Autoscaler
These are the steps to run the autoscaler as a podman container
1. Clone the repository
2. Go to the autoscaler directory in the repository
3. Run the python script with the following command
```python3 autoscaler.py```

## Testing
To test the autoscaler, we can use the Locust tool to generate load on the web application. 
1. Install Locust with the following command
```pip install locust```
2. Run the Locust tool with the following command
```locust -f locustfile.py```
3. Open the browser and go to the URL: http://localhost:8089
4. Enter the number of users and the hatch rate and click on the start button to start the test.

## Authors
- Honnavalli Pranaav