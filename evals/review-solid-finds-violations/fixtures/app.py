import smtplib
from dataclasses import dataclass

import requests


class NotificationSender:
    def send(self, notification):
        channel = notification["channel"]
        message = notification["message"].strip().replace("\n", " ")

        if channel == "email":
            server = smtplib.SMTP("smtp.example.com")
            server.sendmail("noreply@example.com", notification["to"], message)
            server.quit()
        elif channel == "sms":
            requests.post("https://sms.example.com/send", json={"to": notification["to"], "text": message})
        elif channel == "slack":
            requests.post("https://hooks.slack.com/services/XXX", json={"text": message})
        else:
            raise ValueError(f"unknown channel: {channel}")


class BaseRepository:
    def save(self, record):
        raise NotImplementedError

    def delete(self, record):
        raise NotImplementedError


class ReadOnlyAuditRepository(BaseRepository):
    def save(self, record):
        self._log(record)

    def delete(self, record):
        raise RuntimeError("audit records cannot be deleted")

    def _log(self, record):
        pass


@dataclass
class User:
    id: int
    name: str
    email: str
    address: str
    phone: str
    created_at: str
    last_login_at: str
    role: str


class ReportGenerator:
    def generate(self, user: User):
        return f"Report for {user.name} ({user.email})"


class StripeClient:
    def charge(self, amount):
        ...


class OrderProcessor:
    def __init__(self):
        self.payment_client = StripeClient()

    def process(self, order):
        return self.payment_client.charge(order.total)
