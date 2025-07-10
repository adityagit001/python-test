import streamlit as st
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get credentials and numbers from .env
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_FROM_NUMBER')
default_recipient = os.getenv('TWILIO_TO_NUMBER')

# App UI
st.set_page_config(page_title="📱 Twilio SMS Sender", page_icon="📩")
st.title("📩 Send SMS with Twilio")
st.write("Send a message using Python and Twilio")

# Input fields
recipient = st.text_input("Recipient Phone Number", value=default_recipient or "")
message_body = st.text_area("Your Message", height=100)

# Send button
if st.button("Send SMS"):
    if not all([account_sid, auth_token, twilio_number]):
        st.error("❌ Missing Twilio credentials in .env file.")
    elif not recipient or not message_body.strip():
        st.warning("⚠️ Please fill all fields.")
    else:
        try:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=recipient
            )
            st.success(f"✅ Message sent successfully! SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ Failed to send message: {str(e)}")
