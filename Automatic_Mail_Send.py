import smtplib
from email.message import EmailMessage

# 1. Setup your details
sender_email = "your_email@gmail.com"
receiver_email = "recipient@example.com"
app_password = "xxxx xxxx xxxx xxxx" # Your 16-character App Password

# 2. Create the "Envelope"
msg = EmailMessage()
msg['Subject'] = "Hello from Python!"
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content("This is a plain text email sent using smtplib.")

# 3. The Delivery
try:
    # Connecting to Gmail's server (Port 587 is standard for TLS)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() # Secure the connection
        server.login(sender_email, app_password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")