"""Driven adapter: sends the order confirmation over SMTP behind core's NotifierPort."""

import smtplib
from email.message import EmailMessage

from core.ports import NotifierPort


class SmtpNotifier(NotifierPort):
    def __init__(self, host: str, sender: str) -> None:
        self._host = host
        self._sender = sender

    def order_confirmed(self, order_id: str, total_cents: int) -> None:
        message = EmailMessage()
        message["From"] = self._sender
        message["To"] = "orders@example.com"
        message["Subject"] = f"Order {order_id} confirmed"
        message.set_content(f"Total: {total_cents / 100:.2f}")
        with smtplib.SMTP(self._host) as smtp:
            smtp.send_message(message)
