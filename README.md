# Python Email Sender 📧

A simple, reusable Python script to send emails using the `smtplib` and `email` libraries. This project demonstrates how to send plain text messages and attachments (like PNG or PDF files) via Gmail.

## 🚀 Features
- **Plain Text Emails**: Send quick updates or notifications.
- **File Attachments(Auto-Detection)**:  Works for PNG, JPG, PDF, ZIP, and more using the `mimetypes` library.
- **Secure Connection**: Uses `SSL/TLS` for secure communication with mail servers.

## 🛠️ Prerequisites
- Python 3.x
- A Gmail account (or other SMTP provider)
- An **App Password** (Required if using 2FA)

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/m4hmudh4s44n/python-email-sender.git](https://github.com/m4hmudh4s44n/python-email-sender.git)
   ```
   
2. Navigate to the directory:
```bash
cd python-email-sender

```

## 🖥️ Usage

Update the variables in the script with your details:

* `sender_email`: Your email address.
* `app_password`: Your 16-character Google App Password.
* `receiver_email`: The recipient's address.

Run the script:

```bash
python email_sender.py

```

## 🛡️ Security Note

**Never** hardcode your real password. Use environment variables or a `.env` file to keep your credentials safe before pushing to GitHub.

---

### One final tip for your GitHub 🛡️
When you upload this, it is very common for people to accidentally upload their **App Password** inside the code. If a bot finds that password on GitHub, they could use your account to send spam.
