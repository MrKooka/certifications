## What is Kubernetes?
Kubernetes, often abbreviated as K8s, is an open-source platform designed for automating the deployment, scaling, and management of **containerized applications**. It orchestrates clusters of virtual machines and schedules containerized applications to run on these clusters based on the resources available. Kubernetes is highly scalable and supports both stateless and stateful applications.
(Kubernetes обладает высокой масштабируемостью и поддерживает как приложения с отслеживанием состояния, так и без него.)
## Key Concepts:
- **Cluster:** A Kubernetes cluster consists (состоит) of at least one master node and multiple worker nodes. The master node manages the cluster, while worker nodes run the containerized applications.
- **Pod:** The smallest deployable unit in Kubernetes. A pod can contain one or more containers, which share storage, network, and configuration.
- **Node:** A machine (physical or virtual) in the cluster that runs containerized applications. Each node contains the necessary services to run pods.
- **Service:** A way to expose a set of pods as a network service. Services abstract access to pods and handle load balancing across them.
- **Namespace:** A mechanism for isolating groups of resources within a single Kubernetes cluster. It allows for more flexible resource management.
- **Deployment:** A controller that manages stateless applications. It ensures the desired number of pod replicas are running and automatically replaces any failed pods.

## Key Kubernetes Components:
- **Kubelet:** An agent that runs on each node and ensures containers are running inside pods.
- **Kube-API Server:** The front-end of the Kubernetes control plane. It exposes the Kubernetes API and acts as the central management entity for the cluster.
- **etcd:** A consistent and highly available key-value store used by Kubernetes to store all cluster data.
- **Kube-Scheduler:** Responsible for scheduling pods on nodes based on resource availability and other constraints.
- **Kube-Controller-Manager:** Runs controller processes that handle replication and ensuring the desired state of the system.

## Key Features:
- **Automatic Scaling:** Kubernetes can automatically scale applications based on resource usage or custom metrics using Horizontal Pod Autoscalers.
- **Self-Healing:** Kubernetes automatically replaces and reschedules failed containers, ensuring that applications stay available.
- **Service Discovery and Load Balancing:** Kubernetes provides built-in service discovery for pods and distributes network traffic across pods using services.
- **Rolling Updates and Rollbacks:** Kubernetes can perform rolling updates for deployments, ensuring minimal downtime during application updates. It also allows for rollbacks to previous versions in case of failure.

## Common Commands:
- **Create a deployment:**
    ```bash
    kubectl create deployment <name> --image=<container_image>
    ```
- **Scale a deployment:**
    ```bash
    kubectl scale deployment <name> --replicas=<number>
    ```
- **Get information about pods:**
    ```bash
    kubectl get pods
    ```
- **Expose a deployment as a service:**
    ```bash
    kubectl expose deployment <name> --type=LoadBalancer --port=<port>
    ```
- **Check logs of a pod:**
    ```bash
    kubectl logs <pod_name>
    ```

## Advantages of Kubernetes:
- **Scalability:** Kubernetes can easily scale containerized applications horizontally by adding or removing pods based on demand.
- **Portability:** Kubernetes supports running containers on a wide variety of infrastructure, including public clouds, private clouds, and on-premises data centers.
- **Resilience:** Kubernetes monitors the health of applications and automatically restarts containers if they fail.
- **Declarative Management:** Kubernetes allows users to define the desired state of their applications (e.g., number of replicas) and ensures the system maintains that state.

## Use Cases:
- **Microservices:** Kubernetes is ideal for managing microservices architectures, where each service can be run in its own container and scaled independently.
- **CI/CD Pipelines:** Kubernetes facilitates the continuous integration and continuous deployment of applications by automating deployments and scaling.
- **Hybrid Cloud:** Kubernetes supports multi-cloud and hybrid-cloud architectures, making it a good choice for organizations with complex cloud setups.

## Related Tools:
- **Helm:** A package manager for Kubernetes, which simplifies the deployment of applications through reusable "Helm charts."
- **Minikube:** A tool that allows you to run a single-node Kubernetes cluster locally for development and testing.
- **Istio:** A service mesh that integrates with Kubernetes to provide advanced traffic management, security, and monitoring.

## Related Notes:
- [[Docker Basics]]
- [[Containerization vs Virtualization]]
- [[Microservices Architecture]]
- [[LXC]]
