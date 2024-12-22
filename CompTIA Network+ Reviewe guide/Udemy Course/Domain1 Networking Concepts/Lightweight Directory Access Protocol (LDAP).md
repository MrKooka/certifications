### **3. Lightweight Directory Access Protocol (LDAP)**

#### **Purpose**:

- Used to access and manage directory information, such as user accounts, in a hierarchical format.

#### **How It Works**:

- Directories store information (e.g., users, groups, resources) in a tree-like structure.
- LDAP provides a standardized way to query and modify this information.
- Common operations:
    - **Search**: Find user details.
    - **Bind**: Authenticate a user.
    - **Add/Delete/Modify**: Manage directory entries.

#### **Uses**:

- Centralized user authentication (e.g., login to systems or applications).
- Managing corporate directories or address books.

#### **Ports**:

- Default: **TCP/UDP port 389**.
- Secure (LDAPS): **TCP port 636**.

---

### Quick Comparison:

| **Protocol** | **Purpose**                          | **Ports**         |
| ------------ | ------------------------------------ | ----------------- |
| **NTP**      | Synchronize clocks over a network    | UDP 123           |
| **SIP**      | Establish/manage multimedia sessions | TCP/UDP 5060/5061 |
| **LDAP**     | Access/manage directory information  | TCP/UDP 389, 636  |
[[LDAP directory information]]