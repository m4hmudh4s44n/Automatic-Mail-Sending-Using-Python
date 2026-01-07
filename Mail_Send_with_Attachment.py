import smtplib
import mimetypes
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "Universal File Transfer"
msg['From'] = "your_email@gmail.com"
msg['To'] = "recipient@example.com"
msg.set_content("This email was sent using a universal attachment script.")
app_password = "xxxx xxxx xxxx xxxx" # Your 16-character App Password

# Change this to any file: .png, .jpg, .pdf, .zip, .docx, etc.
file_path = "document.pdf" 

# 1. Identify the file type automatically
ctype, encoding = mimetypes.guess_type(file_path)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream' # Default if type is unknown

maintype, subtype = ctype.split('/', 1)

# 2. Read and attach
with open(file_path, 'rb') as f:
    file_data = f.read()
    msg.add_attachment(
        file_data,
        maintype=maintype,
        subtype=subtype,
        filename=file_path
    )

# 3. Secure Delivery
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your_email@gmail.com", "your_app_password")
        server.send_message(msg)
    print(f"Success! {file_path} sent.")
except Exception as e:

    print(f"Error: {e}")
