## What is a Hypervisor?
A hypervisor, also known as a virtual machine monitor (VMM), is software that creates and manages virtual machines (VMs) by allocating hardware resources from a physical host system. It allows multiple operating systems to run concurrently on a single physical machine by virtualizing hardware.

## Types of Hypervisors:
- **Type 1 (Bare-metal Hypervisor):** Runs directly on the hardware, without an underlying (лежащий в основе) operating system. Common examples include VMware ESXi, Microsoft Hyper-V, and Xen.
- **Type 2 (Hosted Hypervisor):** Runs on top of an operating system (OS) and relies on the host OS for resources. Examples include VirtualBox and VMware Workstation.

## Key Functions:
- Virtualizes CPU, memory, storage, and networking resources.
- Manages the execution of multiple guest operating systems.
- Provides isolation between virtual machines, ensuring security and performance.

## Advantages:
- **Resource Efficiency:** Allows better utilization of hardware by running multiple virtual machines on a single host.
- **Isolation:** Keeps virtual machines separate from one another, preventing issues in one VM from affecting others.
- **Scalability:** VMs can be easily cloned, migrated, or adjusted in size to meet changing resource needs.

## Examples of Hypervisors:
- **KVM (Kernel-based Virtual Machine):** A popular open-source Type 1 hypervisor integrated into Linux.
- **VMware ESXi:** A widely used enterprise-level Type 1 hypervisor.
- **VirtualBox:** A free, open-source Type 2 hypervisor used for desktop virtualization.

## Related Notes:
- [[LXC (Linux Containers)]]
- [[Containerization vs Virtualization]]
- [[KVM and VirtualBox Comparison]]
