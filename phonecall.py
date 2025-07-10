import streamlit as st
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Twilio number (fixed)
from_number = os.getenv("TWILIO_FROM_NUMBER")

# Streamlit UI
st.set_page_config(page_title=" Twilio Voice Caller", page_icon="📱")
st.title("Twilio Voice Call Sender")

st.markdown("Send a **voice call** with your custom message using Twilio.")

# Input Fields
to_number = st.text_input("Recipient Number (with country code)", "+91")
message_text = st.text_area("Message to Speak", "Hello! This is a test voice call from Streamlit app.")

# Call Button
if st.button(" Make Call"):
    if not all([account_sid, auth_token, from_number, to_number]):
        st.error("Missing Twilio credentials or phone number.")
    elif not message_text.strip():
        st.warning("Please enter a message to speak.")
    else:
        try:
            # Create Twilio client
            client = Client(account_sid, auth_token)

            # Make the call
            call = client.calls.create(
                twiml=f'<Response><Say voice="alice">{message_text}</Say></Response>',
                to=to_number,
                from_=from_number
            )

            st.success(f" Call initiated! SID: {call.sid}")

            # Fetch latest call info
            latest_call = client.calls(call.sid).fetch()
            st.subheader(" Call Details")
            st.text(f"Status      : {latest_call.status}")
            st.text(f"Start Time  : {latest_call.start_time}")
            st.text(f"End Time    : {latest_call.end_time}")
            st.text(f"To          : {latest_call.to}")
            st.text(f"From        : {latest_call._from}")
            st.text(f"Duration    : {latest_call.duration} seconds")

            # Optional: Print error code if exists
            if hasattr(latest_call, "error_code") and latest_call.error_code:
                st.error(f" Error Code: {latest_call.error_code}")
            else:
                st.success(" No error code  call successful or in progress.")

        except Exception as e:
            st.error(f" Failed to make the call: {str(e)}")
