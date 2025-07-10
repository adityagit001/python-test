import streamlit as st
import pywhatkit
import datetime

st.set_page_config(page_title="WhatsApp Message Sender", page_icon="💬")

st.title("📱 WhatsApp Message Scheduler using Python")

# Input fields
phone_number = st.text_input("Enter Phone Number (with country code)", value="+91")
message = st.text_area("Enter your message")

if st.button("Send Message"):
    if phone_number.strip() == "" or message.strip() == "":
        st.warning("Please fill all fields before sending.")
    else:
        try:
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute + 1

            # Send the message
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

            st.success(f"Message scheduled successfully for {hour}:{minute:02d}!")
        except Exception as e:
            st.error(f"Failed to send message: {e}")
