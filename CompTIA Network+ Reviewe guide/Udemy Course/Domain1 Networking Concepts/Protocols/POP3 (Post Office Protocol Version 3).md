Networking Concepts > Email communication > Application layer > POP3
# POP3 (Post Office Protocol Version 3)

## Overview
**POP3 (Post Office Protocol Version 3)** is a standard protocol used for retrieving emails from a mail server. It operates at the **application layer** of the OSI model and is designed for offline email access.

## Key Features
- **Purpose**: Allows a client to download emails from a server to a local device and optionally delete them from the server.
- **Protocol Type**: Text-based communication protocol.
- **Port Numbers**:
  - **Port 110**: Default port for POP3 communication.
  - **Port 995**: Secure POP3 over SSL/TLS (POP3S).

## POP3 Workflow
1. **Client-Server Connection**: The client connects to the mail server using the POP3 protocol.
2. **Authentication**: The client provides login credentials (username and password) to access the mailbox.
3. **Email Retrieval**: Emails are downloaded to the client’s device.
4. **Deletion**: Emails are optionally deleted from the server after download (depending on the client configuration).

## Benefits
- Simple and lightweight.
- Emails are stored locally, enabling offline access.

## Drawbacks
- No synchronization between the client and server. If the email is deleted locally, it cannot be recovered from the server.
- Lacks advanced features compared to IMAP, such as folder management and multi-device synchronization.

## Security
- **Plaintext Communication**: Standard POP3 (port 110) is unencrypted and insecure.
- **Encrypted Communication**:
  - **SSL/TLS**: Secures the connection over port 995.
  - **STARTTLS**: Upgrades the plaintext connection to encrypted.

## Related Protocols
- **SMTP**: Used for sending emails, often in combination with POP3 for receiving.
- **IMAP**: An alternative to POP3 with support for synchronization and advanced mailbox management.

## Exam Objectives
- Domain1: **Networking Concepts**
  - Application-layer protocols for email retrieval.

## Sources
- **CompTIA Network+ Exam Objectives**
- RFC 1939 (The POP3 Protocol Specification)

---

**Tags**: #networkplus #pop3 #email #application-layer  
**Links**: Related: [[SMTP (Simple Mail Transfer Protocol)]], [[IMAP (Internet Message Access Protocol)]], [[STARTTLS]]
