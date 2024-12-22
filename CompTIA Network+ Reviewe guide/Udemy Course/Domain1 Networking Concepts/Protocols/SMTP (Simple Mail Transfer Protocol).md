Networking Concepts > Email communication > Application layer > SMTP
# SMTP (Simple Mail Transfer Protocol)

## Overview
**SMTP (Simple Mail Transfer Protocol)** is a standard protocol used for sending email messages across networks. It operates at the **application layer** of the OSI model and uses a client-server architecture to relay and deliver emails.

## Key Features
- **Purpose**: Handles outgoing mail (sending emails from a client to a mail server or between mail servers).
- **Protocol Type**: Text-based communication protocol.
- **Port Numbers**:
  - **Port 25**: Default port for SMTP communication (can be blocked due to spam concerns).
  - **Port 587**: Recommended for email submission with STARTTLS encryption.
  - **Port 465**: Deprecated; was previously used for SMTP with SSL encryption.

## SMTP Process
1. **Mail Submission**: The client (e.g., an email application) sends the email to an SMTP server.
2. **Relay**: The SMTP server relays the email to the recipient's mail server via the internet.
3. **Delivery**: The recipient’s mail server stores the email for retrieval via protocols like POP3 or IMAP.

## SMTP Commands
- **HELO/EHLO**: Identify the client to the mail server.
- **MAIL FROM**: Specify the sender's email address.
- **RCPT TO**: Specify the recipient's email address.
- **DATA**: Begin the email content.
- **QUIT**: Terminate the session.

## Encryption and Authentication
Modern SMTP implementations support:
- **STARTTLS**: Encrypts the connection after initiating communication.
- **SMTP-AUTH**: Authenticates the client before sending emails, often using a username and password.

## Related Protocols
- **POP3** and **IMAP**: Used for retrieving emails after delivery.
- **DNS (MX Records)**: SMTP relies on DNS to locate the recipient’s mail server via Mail Exchange (MX) records.

## Common Issues
- **Spam Filtering**: Many ISPs block port 25 to reduce spam, requiring ports like 587 for secure email submission.
- **DNS Misconfigurations**: Incorrect MX records can prevent email delivery.
- **Blacklisting**: Sending servers may be blacklisted for spam-like behavior.

## Exam Objectives
- Domain1: **Networking Concepts**
  - Associated with application-layer protocols and email communication.

## Sources
- **CompTIA Network+ Exam Objectives**
- **RFC 5321**: Defines the SMTP protocol.
- [Further Reading](https://www.ietf.org/rfc/rfc5321.txt)

---

**Tags**: #networkplus #smtp #email #application-layer
**Links**: Related: [[POP3 (Post Office Protocol Version 3)]], [[IMAP (Internet Message Access Protocol)]], [[Network Ports]]
