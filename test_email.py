import os
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SENDER_EMAIL = "aidanlkimberley@gmail.com"
RECIPIENT_EMAIL = "aidan.kimberley@mail.mcgill.ca"
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_test_email():
    """Send a test email to verify the email functionality works"""
    if not GMAIL_APP_PASSWORD:
        logging.error("GMAIL_APP_PASSWORD environment variable not set. Cannot send email.")
        return False
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "McGill Seat Checker - Test Email"
        
        # Add body to email
        body = """This is a test email from your McGill Seat Checker script.

If you receive this email, it means:
✅ Gmail app password is working correctly
✅ Email configuration is set up properly
✅ The script can send notifications

Your seat checker is ready to use!

Best regards,
McGill Seat Checker Bot"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
        
        # Send email
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)
        server.quit()
        
        logging.info("✅ Test email sent successfully!")
        return True
    except Exception as e:
        logging.error(f"❌ Failed to send test email: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing email functionality...")
    success = send_test_email()
    if success:
        print("🎉 Email test successful! Check your McGill email inbox.")
    else:
        print("💥 Email test failed. Check the logs above for details.") 