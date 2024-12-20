## What is Virtualization?
Virtualization involves creating multiple virtual machines (VMs) on a single physical server using a hypervisor. Each VM runs its own full-fledged operating system (OS), which allows for the complete isolation of environments. VMs emulate hardware and provide dedicated (выделенный) resources such as CPU, memory, and storage for each guest OS.

### Pros of Virtualization (Плюсы виртуализации:):
- Full isolation between VMs, offering better security.
- Ability to run different operating systems on the same host.
- Complete OS stack within each VM allows flexibility.

### Cons of Virtualization:
- Resource-heavy: each VM runs a full OS, consuming significant CPU, memory, and storage.
- Slower startup times compared to containers.
- Hypervisor overhead reduces overall performance efficiency.

## What is Containerization?
Containerization isolates applications and their dependencies in lightweight containers that share the host system’s kernel but [maintain isolation at the process](#anchor1) level. Containers run in a shared OS environment, reducing the need for multiple full OS installations.

### Pros of Containerization:
- Lightweight: containers share the host OS, consuming fewer resources.
- Fast startup and shutdown times.
- High density: more containers can run on the same hardware compared to VMs.
- Easy to package, deploy, and replicate applications across different environments.

### Cons of Containerization:
- Less isolation: since containers share the host OS, there’s less isolation compared to VMs.
- Limited OS diversity: all containers must run on the same kernel version as the host.
- Potential security risks if not properly managed.

## Key Differences:
- **Isolation:** VMs offer full isolation by emulating hardware, while containers offer lightweight isolation by sharing the host kernel.
- **Performance:** Containers are more efficient in resource usage since they don't require a full OS for each instance.
- **Use Cases:** Virtualization is better for running multiple OS environments, while containerization is ideal for microservices and scalable application deployments.

## Examples:
- **Virtualization:** VMware, KVM, Hyper-V, VirtualBox.
- **Containerization:** Docker, Kubernetes, LXC.

## Related Notes:
- [[Hypervisor]]
- [[Docker Basics]]
- [[Kubernetes Overview]]
- [[LXC (Linux Containers)]]

#anchor1
"Maintain isolation at the process level" means that in containerization, each container runs its own processes (applications or services) separately from other containers. Although all containers share the same underlying operating system kernel, they are isolated in terms of their file system, network stack, and system resources (like CPU and memory usage). This isolation ensures that one container’s processes don’t interfere with or affect the processes running in another container.

Unlike virtual machines, which isolate entire operating systems, container isolation occurs only at the level of individual processes, creating lightweight, efficient environments that still prevent containers from accessing each other’s resources or processes directly. This makes containers much faster and less resource-intensive than virtual machines but with a trade-off of less robust isolation.