"""Driven adapter: sends the order confirmation over SMTP behind core's NotifierPort."""

import smtplib
from email.message import EmailMessage

from adapters.config import SMTP_HOST
from core.ports import NotifierPort


class SmtpNotifier(NotifierPort):
    def order_confirmed(self, order_id: str, total_cents: int) -> None:
        message = EmailMessage()
        message["From"] = "shop@example.com"
        message["To"] = "orders@example.com"
        message["Subject"] = f"Order {order_id} confirmed"
        message.set_content(f"Total: {total_cents / 100:.2f}")
        with smtplib.SMTP(SMTP_HOST) as smtp:
            smtp.send_message(message)
