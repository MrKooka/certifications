### Load Balancer

**Definition**:  
A Load Balancer is a networking device or software used to distribute network traffic evenly across multiple servers or resources. It helps prevent any single server from becoming overwhelmed, ensuring high availability, reliability, and improved performance of applications or services.

**Key Concepts**:
- **Traffic Distribution**: Load balancers use various algorithms to distribute incoming requests. Common algorithms include:
  - **Round Robin**: Distributes requests sequentially across servers.
  - **Least Connections**: Directs traffic to the server with the fewest active connections.
  - **IP Hash**: Assigns clients to servers based on the client's IP address.
- **Types of Load Balancers**:
  - **Hardware Load Balancers**: Physical devices dedicated to distributing traffic. They offer high performance but can be expensive.
  - **Software Load Balancers**: Software-based solutions that run on standard hardware. They are cost-effective and flexible.
  - **Cloud Load Balancers**: Provided as a service by cloud providers, offering scalability and ease of management.
- **OSI Model**: Load balancers typically operate at OSI Layer 4 (Transport Layer) or Layer 7 (Application Layer):
  - **Layer 4 Load Balancing**: Directs traffic based on IP addresses and TCP/UDP ports.
  - **Layer 7 Load Balancing**: Makes routing decisions based on the content of the request, such as URLs or HTTP headers.

**Advantages**:
- **High Availability**: Distributes traffic across multiple servers, reducing the risk of downtime.
- **Scalability**: Supports the addition of more servers to handle increased traffic.
- **Performance Optimization**: Balances workloads to prevent server overload and maintain efficient response times.

**Use Cases**:
- **Web Servers**: Distributes HTTP/HTTPS requests to multiple web servers to handle large numbers of visitors.
- **Database Clusters**: Balances queries among multiple database servers to optimize response times.
- **Content Delivery**: Routes requests to the nearest or fastest server based on the client’s location.

**Considerations**:
- **Health Checks**: Load balancers perform regular health checks on servers to ensure they are responsive. If a server fails, traffic is redirected to functioning servers.
- **Security**: Load balancers can provide an additional layer of security by hiding the underlying infrastructure from external threats.

**CompTIA Network+ Relevance**:
- Understanding load balancing is essential for network optimization and troubleshooting.
- Network administrators should know how to configure and manage load balancers to ensure efficient resource utilization and high service availability.

**Related Notes**:
- [[Servers]]
- [[Client-Server Model]]
- [[examples load balancers]]
- [[How load balancer works]]
- [[Firewalls]]
- [[Network Geography]]

---

This note is tailored for your Zettelkasten system and aligns with CompTIA Network+ exam concepts.