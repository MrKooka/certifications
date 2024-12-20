# Docker Basics

## What is Docker?
Docker is a platform that automates the deployment, scaling, and management of applications using **containerization**. Docker allows developers to package an application and its dependencies into a lightweight, portable container that can run consistently across various environments. Unlike traditional virtual machines, Docker containers share the host system’s kernel, making them faster and more efficient.

## Key Concepts:
- **Image:** A Docker image is a read-only template that contains the application and its environment, including dependencies, libraries, and configurations. Images are used to create Docker containers.
- **Container:** A container is a runtime instance of a Docker image. Containers are isolated environments where applications run, sharing the host OS kernel.
- **Dockerfile:** A text file that contains the instructions to build a Docker image. It defines the base image, application code, dependencies, and other setup steps.
- **Registry:** A storage and distribution system for Docker images. Docker Hub is the most popular public registry where users can upload, share, and download images.

## Key Docker Commands:
- **Pull an image from a registry:**
    ```bash
    docker pull <image_name>
    ```
- **Run a container:**
    ```bash
    docker run <image_name>
    ```
- **List running containers:**
    ```bash
    docker ps
    ```
- **Build an image from a Dockerfile:**
    ```bash
    docker build -t <image_name> .
    ```
- **Stop a running container:**
    ```bash
    docker stop <container_id>
    ```

## Advantages of Docker:
- **Portability:** Docker containers can run on any system that supports Docker, ensuring consistency (последовательность) across development, testing, and production environments.
- **Efficiency:** Containers share the host OS kernel, reducing the overhead of running multiple operating systems as with virtual machines.
- **Rapid Deployment:** Applications packaged in Docker containers can be deployed quickly, as they include all dependencies and configurations.
- **Isolation:** Containers provide process isolation, preventing interference between applications running on the same host.

## Docker vs. Virtual Machines:
- **Lightweight:** Docker containers are much lighter than virtual machines because they don’t require a full OS.
- **Faster startup times:** Containers can start in seconds, whereas VMs take longer to boot up.
- **Resource Efficiency:** Containers share the OS kernel, leading to more efficient resource usage compared to VMs, which need dedicated resources for each OS.

## Use Cases:
- **Microservices Architecture:** Docker is ideal for running microservices, where each service runs in its own container with its own dependencies.
- **Continuous Integration and Continuous Deployment (CI/CD):** Docker streamlines CI/CD pipelines by ensuring consistent environments for testing, development, and production.
- **Scaling Applications:** Docker makes it easy to scale applications by running multiple instances of containers across different systems.

## Common Tools:
- **Docker Compose:** A tool for defining and running multi-container Docker applications. It allows developers to configure services in a `docker-compose.yml` file and manage them together.
- **Docker Swarm:** A native Docker tool for orchestrating and managing clusters of Docker containers.
- **Kubernetes:** A powerful container orchestration system often used with Docker for managing large-scale containerized applications.

## Related Notes:
- [[Containerization vs Virtualization]]
- [[LXC (Linux Containers)]]
- [[Kubernetes Overview]]
- [[Microservices Architecture]]
