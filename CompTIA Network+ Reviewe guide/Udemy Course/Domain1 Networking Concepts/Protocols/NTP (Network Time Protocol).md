
#### **Purpose**:

- Synchronizes the clocks of computers and devices over a network.

#### **How It Works**:

- Uses a hierarchical system of time sources, with each level called a **stratum**.
- Stratum 0: High-precision devices (atomic clocks, GPS clocks).
- Stratum 1: Servers directly connected to Stratum 0.
- Clients synchronize their clocks with NTP servers by requesting the current time.

#### **Uses**:

- Ensures consistent timestamps across systems (e.g., in databases, logs, or distributed systems).

#### **Ports**:

- Operates on **UDP port 123**.

---

