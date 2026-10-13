import smtplib
from email.message import EmailMessage

from core.ports import NotifierPort


class SmtpNotifier(NotifierPort):
    """Sends the confirmation by mail."""

    def __init__(self, host, sender):
        self._host = host
        self._sender = sender

    def order_confirmed(self, order_id, total_cents):
        message = EmailMessage()
        message["From"] = self._sender
        message["Subject"] = f"Order {order_id} confirmed"
        message.set_content(f"Total: {total_cents / 100:.2f}")
        with smtplib.SMTP(self._host) as smtp:
            smtp.send_message(message)
