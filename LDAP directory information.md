[[Networking]] > Directory Services > LDAP > Directory Information Tree (DIT) > Organizational Units (OUs) > Users > [Specific User]

In the context of **LDAP (Lightweight Directory Access Protocol)**, **directory information** refers to the structured data stored in a **directory service**. This data typically includes hierarchical information about **users, groups, resources, and policies** within an organization or network.

---

### **Key Aspects of Directory Information**:

1. **Hierarchical Structure**:
    
    - Directory information is organized like a tree, with nodes representing entities (users, groups, devices).
    - The top node is called the **root**, and branches represent **organizational units** (e.g., departments).
2. **Entries**:
    
    - Each node in the tree is an **entry**, representing a single entity (e.g., a user or a printer).
    - Entries have **attributes** describing specific details.
3. **Attributes**:
    
    - Each entry is defined by attributes, stored as key-value pairs.
    - Examples:
        - User: `cn=John Doe` (common name), `mail=johndoe@example.com`
        - Group: `cn=IT Team`, `member=cn=John Doe`
4. **Schema**:
    
    - The schema defines what attributes can be included in entries and their format.
    - Ensures consistency across directory entries.

---

### **Types of Information in an LDAP Directory**:

1. **User Information**:
    
    - **Common Name (cn)**: Full name of the user.
    - **Username (uid)**: Unique identifier for the user.
    - **Email Address (mail)**: User’s email address.
    - **Password (userPassword)**: Encrypted password for authentication.
2. **Group Information**:
    
    - **Group Name (cn)**: Name of the group.
    - **Members (member)**: List of users in the group.
3. **Organizational Information**:
    
    - **Organization Name (o)**: Name of the organization.
    - **Organizational Unit (ou)**: Department or team within the organization.
4. **Device Information**:
    
    - **Printer Name**: Identifier for a printer.
    - **Device Location**: Physical location of the device.
5. **Policy Information**:
    
    - Access control rules (e.g., who can read or write data).
    - Password expiration policies.

---

### **Example LDAP Tree**:

```
dc=example,dc=com  (Domain Component)
├── ou=Employees   (Organizational Unit)
│   ├── cn=Alice Smith  (User Entry)
│   │   ├── mail=alice@example.com
│   │   ├── uid=asmith
│   │   └── userPassword=********
│   └── cn=Bob Johnson
│       ├── mail=bob@example.com
│       ├── uid=bjohnson
│       └── userPassword=********
├── ou=Groups
│   ├── cn=HR Team
│   │   └── member=cn=Alice Smith,ou=Employees,dc=example,dc=com
│   └── cn=IT Team
│       └── member=cn=Bob Johnson,ou=Employees,dc=example,dc=com
```

---

### **How is Directory Information Used?**

1. **Authentication**:
    - Validating user credentials during login.
2. **Authorization**:
    - Determining a user’s access to resources (e.g., files, applications).
3. **Contact Information**:
    - Providing user details (e.g., email addresses) in corporate address books.
4. **Centralized Management**:
    - Enabling IT teams to manage users and resources from a single location.

---

Would you like to see how LDAP queries work to retrieve directory information? 😊