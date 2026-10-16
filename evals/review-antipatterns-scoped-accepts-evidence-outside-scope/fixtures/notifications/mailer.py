"""Sends the order confirmation emails."""

import smtplib

from orders.settings import SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT_SECONDS


def send(message):
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=SMTP_TIMEOUT_SECONDS) as client:
        client.send_message(message)
