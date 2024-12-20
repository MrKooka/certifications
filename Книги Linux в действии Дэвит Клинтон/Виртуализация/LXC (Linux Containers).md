## What is LXC?
LXC (Linux Containers) is a lightweight virtualization method that provides process-level isolation. It uses containers to run multiple isolated Linux systems (containers) on a single host system, all sharing the same Linux kernel. Unlike virtual machines, LXC containers don’t require a separate operating system for each instance, making them more efficient in terms of resource usage.

## Key Features:
- **Lightweight:** LXC containers share the host OS kernel, making them faster and more resource-efficient compared to full virtual machines.
- **Process-Level Isolation:** Containers maintain isolation at the process level, meaning each container runs its own processes independently from other containers.
- **Network Virtualization:** Containers can have their own virtual network interfaces, IP addresses, and routing, allowing them to act as standalone network entities.
- **Root File System Isolation:** Each container has its own isolated root filesystem, creating separation from the host system.

## How LXC Works:
- **Shared Kernel:** All LXC containers share the Linux kernel of the host system, so they can't run different OS types (like Windows or BSD).
- **Namespaces:** LXC uses Linux namespaces to provide isolation in areas such as process IDs, file system structure, and networking.
- **Control Groups (cgroups):** Cgroups are used to manage and limit the resource usage (CPU, memory, disk I/O, etc.) of containers, ensuring fair resource allocation.

## Common Use Cases:
- **Development and Testing:** LXC is useful for quickly spinning up isolated environments for testing applications in different configurations.
- **Microservices:** Containers can be used to deploy microservices in isolated environments while sharing resources efficiently.
- **Server Consolidation:** Multiple lightweight containers can run services on a single host, reducing the need for multiple physical machines or VMs.

## Commands:
- **Create a container:**
    ```bash
    lxc-create -n <container_name> -t <template>
    ```
- **Start a container:**
    ```bash
    lxc-start -n <container_name>
    ```
- **Stop a container:**
    ```bash
    lxc-stop -n <container_name>
    ```
- **Attach to a running container:**
    ```bash
    lxc-attach -n <container_name>
    ```

## Advantages of LXC:
- **Efficiency:** Containers are more efficient than VMs as they share the host's kernel, leading to lower overhead and faster performance.
- **Portability:** Containers can be easily moved between different systems as they encapsulate the application and its dependencies.
- **Flexibility:** LXC provides granular control over system resources and container configurations.

## Related Notes:
- [[Containerization vs Virtualization]]
- [[Docker Basics]]
- [[Kubernetes Overview]]
- [[Hypervisor]]
