"""Driven adapter: sends the order confirmation over SMTP behind core's NotifierPort."""

import smtplib
from email.message import EmailMessage

from core.ports import NotifierPort
from notifications.templates import confirmation_body


class SmtpNotifier(NotifierPort):
    def __init__(self, host: str, sender: str) -> None:
        self._host = host
        self._sender = sender

    def order_confirmed(self, order_id: str, total_cents: int, subject: str) -> None:
        message = EmailMessage()
        message["From"] = self._sender
        message["To"] = "orders@example.com"
        message["Subject"] = subject
        message.set_content(confirmation_body(total_cents))
        with smtplib.SMTP(self._host) as smtp:
            smtp.send_message(message)
