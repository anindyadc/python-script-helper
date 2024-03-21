import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Test Email from AWS SES'

    # Add body to the email
    body = "This is a test email sent using AWS SES SMTP."
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()  # Start TLS encryption
        server.login(smtp_username, smtp_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print("Email sent successfully!")
        
    except Exception as e:
        print("Failed to send email:", e)
        
    finally:
        # Close the connection to the SMTP server
        server.quit()

def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes.decode('utf-8')

# Replace these values with your AWS SES SMTP credentials and email addresses
sender_email = 'anindya@mashmari.in'
recipient_email = 'anindya@mashmari.in'
smtp_server = 'email-smtp.ap-south-1.amazonaws.com'
smtp_port = 587  # For TLS
smtp_username = 'AKIAQ3EGRNNQQ6B5LEXY'
smtp_password = 'BM5OzRE5S6xki0+jr5iY65YQCIYOuJCe8xk+Qe0Icz2k'

# Decode the Base64 encoded password
# smtp_password = decode_base64(encoded_password)

# Send the email
send_email(sender_email, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password)
