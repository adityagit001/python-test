from twilio.rest import Client
import os

# Step 1: Load from environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Step 2: Set your Twilio number and recipient number
twilio_number = '+19066282681'
recipient_number = '+917691033608'

# Step 3: Create the client and send SMS
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='This is a new message from Python!',
    from_=twilio_number,
    to=recipient_number
)

print(f"✅ Message sent with SID: {message.sid}")
