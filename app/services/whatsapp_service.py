from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(account_sid, auth_token)

def send_whatsapp_message(phone_number: str):
    message = client.messages.create(
        body="Thank you for contacting BV Homes. Our team will reach out shortly.",
        from_=twilio_number,
        to=f"whatsapp:+91{phone_number}"
    )
    return message.sid
