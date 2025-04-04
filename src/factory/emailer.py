import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Emailer:
    def __init__(self, smtp_server, smtp_port, sender_email, password):
        """
        Initialize email sender with SMTP server details
        Args:
            smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
            smtp_port: SMTP port (e.g., 587 for TLS)
            sender_email: Email address to send from
            password: Email account password or app-specific password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Send an email with the specified content
        Args:
            recipient_email: Email address to send to
            subject: Email subject
            body: Email body content (can be HTML)
        """
        # Create message
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "html"))

        try:
            # Create SMTP_SSL session for Hostinger
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, timeout=30) as server:
                server.login(self.sender_email, self.password)
                
                # Send email
                server.send_message(message)
            return True
        except smtplib.SMTPAuthenticationError as e:
            print(f"Authentication failed: {str(e)}")
            return False
        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {str(e)}")
            return False
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False

if __name__ == "__main__":
    pass 