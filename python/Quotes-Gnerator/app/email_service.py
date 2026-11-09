import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv


def send_email(body, recipient):
    # Load environment variables when the function is called
    load_dotenv()
    # Load and validate email credentials
    my_email = os.getenv("EMAIL_ADDRESS")
    if not my_email:
        raise ValueError("EMAIL_ADDRESS is missing from .env")
    password = os.getenv("EMAIL_APP_PASSWORD")
    if not password:
        raise ValueError("EMAIL_APP_PASSWORD is missing from .env")

    # Create the email message
    msg = EmailMessage()
    msg["Subject"] = "Quote of the Day"
    msg["From"] = my_email
    msg["To"] = recipient
    msg.set_content(body)

    # Establish a secure SMTP connection
    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
        connection.starttls(context=context)
        connection.login(user=my_email, password=password)
        connection.send_message(msg)

    return True