import os
import sys

from app.email_service import send_email
from app.logger import logger
from app.quote_service import generate_quote, load_quotes
from dotenv import load_dotenv

try:
    load_dotenv()
    recipient = os.getenv("RECIPIENT_EMAIL")

    if not recipient:
        raise ValueError("RECIPIENT_EMAIL is missing from .env")


    quotes = load_quotes()
    data = generate_quote(quotes)

    body = f"{data['quote']}\n\n— {data['author']}"

    send_email(body, recipient)
    logger.info("Quote email sent successfully to %s", recipient)

except Exception:
    logger.exception("Application failed")
    sys.exit(1)

