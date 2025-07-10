import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

if not EMAIL_ADDRESS or not EMAIL_PASSWORD or not RECEIVER_EMAIL:
    raise ValueError("Missing email credentials!")

# Create SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Email message
message = "This is a test email sent from Python!"

# Send the email
s.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, message)
s.quit()
