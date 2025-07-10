from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = "+19066282681"
to_number ="+917691033608"

if not all([account_sid, auth_token, from_number, to_number]):
    raise ValueError("Missing environment variables!")

client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    twiml='<Response><Say voice="alice">Hello! mohit singh is very best lccn dog in the world.</Say></Response>',
    to=to_number,
    from_=from_number
)

print("📞 Call SID:", call.sid)

# Fetch the call object
latest_call = client.calls(call.sid).fetch()

# Print call info
print("📟 Call Status:", latest_call.status)
print("🕒 Start Time:", latest_call.start_time)
print("🚫 End Time:", latest_call.end_time)
print("📲 To:", latest_call.to)
print("📤 From:", latest_call._from)
print("⏱️ Duration (sec):", latest_call.duration)

# Safely print error code if it exists
if hasattr(latest_call, "error_code") and latest_call.error_code:
    print("❗ Error Code:", latest_call.error_code)
else:
    print("✅ No error code – call likely in progress or successful.")
