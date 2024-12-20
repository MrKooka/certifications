[[Networking]] > [[OSI Model Overview|OSI ModelProtocols]] > [[All OSI Protools|Protools]] > [[Application Layer (Layer 7)|Application Layer]] > Simple Network Management Protocol (SNMP)
### **SNMP (Simple Network Management Protocol)**

#### **What is SNMP?**

SNMP is a protocol used to manage and monitor devices on a network. It helps administrators collect and organize information about connected devices and allows them to remotely configure or troubleshoot those devices.

---

#### **Purpose**:

- **Monitor network devices** (like routers, switches, printers, servers, etc.).
- **Manage configurations** and troubleshoot network issues.
- **Receive alerts** about network performance or failures.

---

#### **How SNMP Works**:

SNMP operates using a **client-server model**, where:

1. **Agents**: Software running on network devices collects and stores device information.
2. **Manager**: The central system (or server) communicates with agents to retrieve or update device data.

SNMP exchanges information using **Management Information Bases (MIBs)**, which are structured databases that define what data can be accessed or modified.

---

#### **SNMP Versions**:

1. **SNMPv1**: The first version, simple but lacks strong security.
2. **SNMPv2**: Improved performance and functionality but still has weak security.
3. **SNMPv3**: Adds strong authentication and encryption for secure communications.

---

#### **Components**:

1. **SNMP Manager**: Centralized application to monitor devices.
2. **SNMP Agent**: Software running on each managed device.
3. **MIB (Management Information Base)**: A database schema that defines the data structure and attributes that can be monitored or configured.

---

#### **Communication in SNMP**:

- **Get Request**: Manager requests information from an agent.
- **Set Request**: Manager updates or configures information on an agent.
- **Trap/Notification**: Agent sends unsolicited alerts to the manager about events like errors or thresholds being exceeded.

---

#### **Works On**:

- **UDP Ports**: 161 (for requests) and 162 (for traps).

---

#### **Examples of Use**:

1. Monitoring CPU usage or memory utilization of a server.
2. Checking the status of a router or switch port.
3. Receiving alerts when a device goes offline.

---

#### **Advantages**:

- Efficient for large-scale network management.
- Real-time alerts for network events.
- Compatible with a wide range of devices.

#### **Limitations**:

- Older versions (SNMPv1 and v2) have weak security.
- Relies on UDP, which doesn’t guarantee message delivery.

---

Would you like to know how SNMP compares to other network management protocols? 😊

[[Prometheus and SNMP]]
