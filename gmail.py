import streamlit as st
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

st.set_page_config(page_title="📧 Send Email App", layout="centered")
st.title(" Send Email with Python")

# Form for email subject and message
with st.form("email_form"):
    subject = st.text_input("Subject", "Test Email from Streamlit")
    message_body = st.text_area("Message", "This is a test email sent using Streamlit!")
    send_button = st.form_submit_button("Send Email")

    if send_button:
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD or not RECEIVER_EMAIL:
            st.error("Missing email credentials in .env file!")
        else:
            try:
                # Compose the full message
                message = f"Subject: {subject}\n\n{message_body}"
                
                # Send the email
                with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                    smtp.starttls()
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, message)

                st.success(f" Email sent to {RECEIVER_EMAIL} successfully!")
            except Exception as e:
                st.error(f" Failed to send email: {e}")
