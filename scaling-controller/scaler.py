import time
import requests
import subprocess

# HAProxy stats endpoint URL
stats_url = "http://localhost:8080/stats"

# Scaling thresholds
scale_up_threshold = 20
scale_down_threshold = 10

# Container management commands
start_container_cmd = "podman run -d webapp"
stop_container_cmd = "podman stop {}"

# Function to scale up containers
def scale_up_containers(num_containers):
    for _ in range(num_containers):
        subprocess.run(start_container_cmd, shell=True)

# Function to scale down containers
def scale_down_containers(num_containers):
    containers = subprocess.check_output("podman ps -q", shell=True).decode().splitlines()
    containers_to_stop = containers[:num_containers]
    for container in containers_to_stop:
        subprocess.run(stop_container_cmd.format(container), shell=True)

# Function to check activity and bring down idle containers
def check_activity():
    containers = subprocess.check_output("podman ps -q", shell=True).decode().splitlines()
    active_containers = []
    for container in containers:
        container_stats_url = f"http://{container}:8080/stats"
        try:
            response = requests.get(container_stats_url)
            if response.status_code == 200:
                active_containers.append(container)
        except requests.exceptions.RequestException:
            pass
    if len(active_containers) > 1:
        containers_to_stop = active_containers[1:]
        for container in containers_to_stop:
            subprocess.run(stop_container_cmd.format(container), shell=True)

# Main loop
while True:
    try:
        response = requests.get(stats_url)
        if response.status_code == 200:
            stats = response.json()
            total_requests = int(stats["total_requests"])
            containers = subprocess.check_output("podman ps -q", shell=True).decode().splitlines()
            num_containers = len(containers)
            if total_requests > scale_up_threshold * num_containers:
                scale_up_containers(1)
            elif total_requests < scale_down_threshold * num_containers and num_containers > 1:
                scale_down_containers(1)
            check_activity()
    except requests.exceptions.RequestException:
        pass
    time.sleep(15)
