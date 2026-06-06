# Python Email Client

A simple Python project for learning how email works behind the scenes using Gmail, SMTP, and IMAP.

This project demonstrates how emails are sent and received using Python's built-in networking libraries and Google's mail servers.

## Project Structure

```
python-email-client/
├── send_email.py
├── receive_email.py
└── README.md
```

## Overview

Email communication relies on different protocols:

- **SMTP (Simple Mail Transfer Protocol)** for sending emails.
- **IMAP (Internet Message Access Protocol)** for receiving and managing emails.

This project implements both protocols using Python and Gmail.

## Features

### Email Sending

- Gmail SMTP authentication
- Custom recipient support
- Custom subject lines
- Custom message content
- Multiple emails in a single session

### Email Receiving

- Gmail IMAP authentication
- Inbox access
- Unread email detection
- Email header decoding
- Email content extraction

## Files

### send email.py

Allows users to:

- Log in using a Gmail address and App Password
- Create email messages
- Send emails through Gmail's SMTP server
- Continue sending emails without restarting the program

### receive email.py

Allows users to:

- Connect to Gmail using IMAP
- Access inbox messages
- Search for unread emails
- Decode email headers
- Process received messages

## Technologies Used

- Python
- smtplib
- imaplib
- email

## How It Works

### Sending Emails

1. User enters a Gmail address.
2. User enters a Gmail App Password.
3. Program creates an email message.
4. SMTP connection is established.
5. Message is transmitted through Gmail's servers.

### Receiving Emails

1. User authenticates with Gmail.
2. IMAP connection is established.
3. Inbox is accessed.
4. Unread messages are searched.
5. Email data is decoded and processed.

## Learning Objectives

This project was created to explore:

- Computer networking fundamentals
- Email infrastructure
- SMTP communication
- IMAP communication
- Authentication systems
- Python networking libraries
- Email message formatting

## Security Notice

Do not upload or share:

- Personal email credentials
- Gmail App Passwords
- Sensitive account information

When publishing projects online, always remove credentials and sensitive data.

## Future Improvements

- HTML email support
- File attachments
- Inbox filtering
- Email search functionality
- Better error handling
- Command-line arguments
- Graphical user interface (GUI)
- Email logging system

## Example Use Cases

- Learning SMTP and IMAP protocols
- Understanding how email systems work
- Practicing Python networking
- Educational networking projects
- Building more advanced mail clients

## License

This project is intended for educational and learning purposes.
