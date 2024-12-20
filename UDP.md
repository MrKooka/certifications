[[Networking]] > [[OSI Model Overview|OSI Model]] > [[Transport Layer]] > User Datagram Protocol (UDP


### **Overview**

- **UDP** is a transport layer protocol (Layer 4 of the OSI model) that provides a connectionless, lightweight data transfer mechanism.
- It is often used in applications where speed is critical and reliability is less important.

---

### **Key Features of UDP**

1. **Connectionless Protocol**:
    
    - No handshake process (like TCP's three-way handshake).
    - Data is sent without establishing a connection between sender and receiver.
2. **Unreliable**:
    
    - No guarantee of data delivery, order, or integrity.
    - No error-checking or retransmission mechanisms.
3. **Lightweight**:
    
    - Minimal overhead, making it faster and more efficient than TCP.
    - Header size is only 8 bytes compared to TCP's 20 bytes.
4. **Broadcast and Multicast Support**:
    
    - Ideal for broadcasting or multicasting data to multiple recipients.

---

### **UDP Header Format**

The **UDP header** consists of:

1. **Source Port (16 bits)**: Identifies the sender's port.
2. **Destination Port (16 bits)**: Identifies the receiver's port.
3. **Length (16 bits)**: Specifies the length of the UDP header and data.
4. **Checksum (16 bits)**: Ensures data integrity but is optional.

---

### **Use Cases**

UDP is suitable for applications requiring low latency and real-time data transfer. Examples:

- **Streaming**: Video/audio streaming services like Netflix or VoIP (Voice over IP).
- **Online Gaming**: Real-time multiplayer games.
- **DNS (Domain Name System)**: Quick query responses.
- **TFTP (Trivial File Transfer Protocol)**: Simple, lightweight file transfer.

---

### **UDP vs TCP**

|Feature|UDP|TCP|
|---|---|---|
|**Connection Type**|Connectionless|Connection-oriented|
|**Reliability**|Unreliable|Reliable (data acknowledgment)|
|**Speed**|Faster (no handshake, minimal)|Slower (due to acknowledgments)|
|**Data Integrity**|Not guaranteed|Guaranteed (through sequencing)|
|**Use Cases**|Real-time apps, streaming|File transfers, emails, web apps|

---

### **Protocols Using UDP**

- **DNS**: Resolving domain names into IP addresses.
- **DHCP**: Assigning IP addresses to devices dynamically.
- **SNMP**: Managing devices in a network.
- **RIP**: Routing protocol for sharing routing information.
- **NTP**: Synchronizing time across devices.

---

### **Exam Tips**

1. **Identify UDP Use Cases**: Be familiar with scenarios where UDP is preferred over TCP.
2. **Differentiate UDP from TCP**: Understand their advantages and limitations.
3. **Recognize Port Numbers**:
    - DNS (Port 53)
    - TFTP (Port 69)
    - DHCP (Ports 67/68)
    - SNMP (Ports 161/162)
    - NTP (Port 123)
4. **Understand Headers**: Be ready to interpret the simple structure of the UDP header.

---
