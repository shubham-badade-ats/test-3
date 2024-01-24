# import docker

# def remove_old_image(client, image_name):
#     try:
#         client.images.remove(image_name, force=True)
#         print(f"Removed existing Docker image: {image_name}")
#     except docker.errors.ImageNotFound:
#         print(f"Docker image not found: {image_name}")

# def pull_latest_image(client, image_name):
#     print(f"Pulling the latest version of Docker image: {image_name}")
#     client.images.pull(image_name)

# def run_container(client, image_name):
#     print(f"Running a container from the updated image: {image_name}")
#     container = client.containers.run(image_name, detach=True)
#     print(f"Container ID: {container.id}")

# def main():
#     # Set the name of the Docker image
#     image_name = "docker-test"

#     # Create a Docker client
#     client = docker.from_env()

#     # Remove the existing Docker image
#     remove_old_image(client, shubhambadade07/test)

#     # Pull the latest version of the Docker image
#     pull_latest_image(client, shubhambadade07/test)

#     # Run a container from the updated image
#     run_container(client, shubhambadade07/test)

# if __name__ == "__main__":
#     main()



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
    container_id = subprocess.run(["docker", "run", "-d", image_name], check=True, capture_output=True, text=True).stdout.strip()
    print(f"Container ID: {container_id}")

def main():
    # Set the name of the Docker image
    image_name = "docker-test"

    # Remove the existing Docker image
    remove_old_image("shubhambadade07/new-test")

    # Pull the latest version of the Docker image
    pull_latest_image("shubhambadade07/new-test")

    # Run a container from the updated image
    run_container("shubhambadade07/new-test")

if __name__ == "__main__":
    main()
