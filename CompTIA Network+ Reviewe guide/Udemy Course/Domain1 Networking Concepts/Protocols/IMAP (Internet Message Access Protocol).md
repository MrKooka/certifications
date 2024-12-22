Networking Concepts > Email communication > Application layer > IMAP
## Overview
**IMAP (Internet Message Access Protocol)** is a standard protocol for retrieving and managing email messages from a mail server. It operates at the **application layer** of the OSI model and is designed for modern multi-device email access.

## Key Features
- **Purpose**: Allows users to access and manage their emails directly on the mail server without downloading them permanently.
- **Protocol Type**: Text-based communication protocol.
- **Port Numbers**:
  - **Port 143**: Default port for IMAP communication.
  - **Port 993**: Secure IMAP over SSL/TLS (IMAPS).

## IMAP Workflow
1. **Server Connection**: The client connects to the mail server using IMAP.
2. **Email Synchronization**:
   - Emails are stored on the server and synchronized with all connected devices.
   - Changes (e.g., read/unread status, folder organization) are reflected on all devices.
3. **Partial Download**:
   - Only headers or parts of emails are downloaded initially, improving performance for large messages.

## Benefits
- **Multi-Device Access**: Perfect for users accessing emails on multiple devices (e.g., smartphone, tablet, PC).
- **Server-Side Storage**: Emails remain on the server unless explicitly deleted, preventing accidental loss.
- **Advanced Features**: Supports folder management, searching messages on the server, and selective downloading.

## Drawbacks
- **Server Dependency**: Requires an active internet connection to access emails.
- **Storage Limits**: Server-side storage may become full if emails aren’t deleted or archived regularly.

## Security
- **Encryption**:
  - **SSL/TLS**: Encrypted communication over port 993.
  - **STARTTLS**: Upgrades plaintext connections over port 143 to encrypted connections.
- Modern IMAP servers require authentication and encryption to prevent data interception and unauthorized access.

## Related Protocols
- **SMTP**: Used in combination with IMAP for sending emails.
- **POP3**: An alternative to IMAP for email retrieval, with limited synchronization capabilities.

## Common Use Cases
- Web-based email providers like Gmail, Outlook, Yahoo Mail, and enterprise email solutions.
- Synchronizing emails across devices while keeping data centrally stored on the server.

## Exam Objectives
- Domain1: **Networking Concepts**
  - Application-layer protocols for email retrieval.

## Sources
- **CompTIA Network+ Exam Objectives**
- RFC 3501 (IMAP Version 4)

---

**Tags**: #networkplus #imap #email #application-layer  
**Links**: Related: [[SMTP (Simple Mail Transfer Protocol)]], [[POP3 (Post Office Protocol Version 3)]], [[STARTTLS]]
