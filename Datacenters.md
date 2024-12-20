Any facility that businnesses and other organizations use to organized precess store and disseminate large amount of data

Architectures:
1. Three-tiered hierarchy 
2. Collapsed core 
3. Spine and leaf architecture 
4. Traffic flows 

### **Three-tiered hierarchy** 

![[Pasted image 20241204141425.png]]

The three-tiered architecture is a traditional network design for data centers, consisting of three layers:

- **Core Layer:**
    
    - Acts as the backbone of the network.
    - Provides high-speed connectivity between aggregation layers or directly to external networks.
    - Now, the core layer consist of the biggest, fastest and most expensive routers 
    - Designed for scalability and redundancy.
- **Aggregation Layer (or Distribution Layer):**
    
    - Connects the access layer to the core layer.
    - Manages routing, filtering, and network policy enforcement. Here at the distribution or aggregation layer, we're efining the policies  for networks at large.
    - Aggregates traffic from multiple access layers.
- **Access Layer:**
    
    - The layer closest to servers, storage devices, and end-user devices.
    - Provides connectivity to hosts in the data center.
    - Typically uses switches to connect servers to the network.

**Pros:**

- Well-structured and scalable for traditional workloads.

**Cons:**

- Higher latency due to multiple layers.
- Limited flexibility for modern, dynamic workloads.
---
### **2. Collapsed Core**

A **collapsed core** architecture combines the **core** and **aggregation** layers into a single layer:

- **Purpose:**
    
    - Simplifies network design for smaller data centers or environments where a full three-tiered hierarchy is unnecessary.
- **Advantages:**
    
    - Lower costs by reducing the number of devices and interconnections.
    - Simplified management and reduced complexity.
- **Disadvantages:**
    
    - May become a bottleneck as traffic grows.
    - Limited scalability compared to the three-tiered model.

---

### **3. Spine-and-Leaf Architecture**

The **spine-and-leaf architecture** is a modern network design used in high-performance data centers:

- **Spine Layer:**
    
    - A set of high-speed switches that act as the backbone.
    - Provides connectivity between leaf switches.
- **Leaf Layer:**
    
    - A set of switches that connect directly to servers and storage devices.
    - All leaf switches are connected to all spine switches, creating a fully meshed network.

**Key Features:**

- **Low Latency:** Equal number of hops between any two devices.
- **High Throughput:** Full bandwidth is available between any two nodes.
- **Scalability:** New spines or leaves can be added without reconfiguring the network.

**Comparison to Three-Tiered Architecture:**

- Spine-and-leaf focuses on east-west traffic (between servers) rather than north-south traffic (server to internet) predominant in the three-tiered model.

---

### **4. Traffic Flows in Data Centers**

Data center traffic flows can be categorized into two main types:

- **North-South Traffic:**
    
    - Traffic that flows between internal data center devices and external networks (e.g., internet).
    - Dominant in traditional client-server models.
- **East-West Traffic:**
    
    - Traffic that flows between servers within the data center.
    - Crucial for modern applications like distributed databases, microservices, and big data analytics.
    - Requires low-latency, high-bandwidth interconnections, which spine-and-leaf architecture is optimized for.

**Trends in Traffic Flows:**

- Modern data centers see a significant shift toward east-west traffic due to cloud computing, virtualization, and distributed workloads.
- Architectures like spine-and-leaf are designed to accommodate this shift.

---

Let me know if you'd like detailed diagrams or Zettelkasten-style notes on these topics!