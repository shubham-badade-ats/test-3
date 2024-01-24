import subprocess

def remove_old_image(image_name):
    try:
        subprocess.run(["docker", "rmi", image_name, "-f"], check=True)
        print(f"Removed existing Docker image: {image_name}")
    except subprocess.CalledProcessError:
        print(f"Docker image not found: {image_name}")

def pull_latest_image(image_name):
    print(f"Pulling the latest version of Docker image: {image_name}")
    subprocess.run(["docker", "pull", image_name], check=True)

def run_container(image_name):
    print(f"Running a container from the updated image: {image_name}")
    container_id = subprocess.run(["docker", "run", "-d", "-p", "4200:4200", "--name", "test", image_name], check=True, capture_output=True, text=True).stdout.strip()
    print(f"Container ID: {container_id}")

def stop_and_remove_container(container_name):
    try:
        subprocess.run(["docker", "stop", container_name], check=True)
        print(f"Stopped Docker container: {container_name}")
        subprocess.run(["docker", "rm", container_name], check=True)
        print(f"Removed Docker container: {container_name}")
    except subprocess.CalledProcessError:
        print(f"Error stopping or removing Docker container: {container_name}")

def main():
    # Set the name of the Docker image and container
    image_name = "shubhambadade07/new-test"
    container_name = "test"
    # Stop and remove the container by name
    stop_and_remove_container(container_name)

    # Remove the existing Docker image
    remove_old_image(image_name)

    # Pull the latest version of the Docker image
    pull_latest_image(image_name)

    # Run a container from the updated image
    run_container(image_name)

    
    

if __name__ == "__main__":
    main()
