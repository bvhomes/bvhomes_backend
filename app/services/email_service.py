import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_lead_notification(lead):
    msg = EmailMessage()
    msg["Subject"] = f"New Lead for Product ID {lead.product_id}"
    msg["From"] = SMTP_EMAIL
    msg["To"] = SMTP_EMAIL

    msg.set_content(f"""
New Lead Received:

Name: {lead.name}
Email: {lead.email}
Phone: {lead.phone}
City: {lead.city}
Product ID: {lead.product_id}
Message: {lead.message}
""")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
