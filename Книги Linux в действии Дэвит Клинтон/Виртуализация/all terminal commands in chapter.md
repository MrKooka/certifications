| **Command**                                                   | **Description**                                 |
| ------------------------------------------------------------- | ----------------------------------------------- |
| `vboxmanage clonevm <vm_name> --name <clone_name> --register` | Create a full clone of a VirtualBox VM.         |
| `vboxmanage list vms`                                         | List all virtual machines in VirtualBox.        |
| `vboxmanage startvm <vm_name>`                                | Start a VirtualBox virtual machine.             |
| `vboxmanage controlvm <vm_name> poweroff`                     | Stop a running VirtualBox virtual machine.      |
| `lxc-create -n <container_name> -t <template>`                | Create a new LXC container based on a template. |
| `lxc-start -n <container_name>`                               | Start an LXC container.                         |
| `lxc-stop -n <container_name>`                                | Stop a running LXC container.                   |
| `lxc-attach -n <container_name>`                              | Attach to a running LXC container.              |
| `lxc-ls --fancy`                                              | List all LXC containers with detailed info.     |
| `lxc-attach -n <container_name> -- reboot`                    | Reboot an LXC container.                        |
| `lxc-attach -n <container_name> -- ip addr`                   | Show the IP address of an LXC container.        |
| `vboxmanage export <vm_name> -o <file_name>.ova`              | Export a VirtualBox VM to an OVA file.          |
| `vboxmanage import <file_name>.ova`                           | Import a VM from an OVA file in VirtualBox.     |
| `scp <file_path> username@<remote_ip>:/path/to/destination`   | Copy a file to a remote machine using SCP.      |
