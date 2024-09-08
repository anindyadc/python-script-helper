import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SendGrid SMTP server configuration
SMTP_SERVER = 'smtp.sendgrid.net'
SMTP_PORT = 587  # Use 465 for SSL
SMTP_USERNAME = 'apikey'  # This is the literal string 'apikey'
SMTP_PASSWORD = 'SG.Pez4TC7Y1p4Q4wwTQ.CGC83MmeMmADKYjNqYM_4KaxQO4'

# Email content
FROM_EMAIL = 'ani@from.com'
TO_EMAIL = 'ani@to.com'
SUBJECT = 'Test Email from SendGrid SMTP'
BODY = 'This is a test email sent using SendGrid SMTP server.'

def send_email():
    # Create message
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    # Attach body
    msg.attach(MIMEText(BODY, 'plain'))

    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to secure TLS
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

if __name__ == '__main__':
    send_email()
