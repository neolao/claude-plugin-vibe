from dataclasses import dataclass
from typing import Protocol


class Notifier(Protocol):
    def send(self, to: str, message: str) -> None: ...


class EmailNotifier:
    def send(self, to: str, message: str) -> None:
        ...  # SMTP call


class SmsNotifier:
    def send(self, to: str, message: str) -> None:
        ...  # SMS gateway call


NOTIFIERS: dict[str, Notifier] = {}


def register_notifier(channel: str, notifier: Notifier) -> None:
    NOTIFIERS[channel] = notifier


def send_notification(channel: str, to: str, message: str) -> None:
    NOTIFIERS[channel].send(to, message)


@dataclass
class UserContact:
    name: str
    email: str


def format_greeting(contact: UserContact) -> str:
    return f"Hello {contact.name}, we'll reach you at {contact.email}"


class PaymentGateway(Protocol):
    def charge(self, amount: int) -> None: ...


class OrderProcessor:
    def __init__(self, payment_gateway: PaymentGateway):
        self._payment_gateway = payment_gateway

    def process(self, total: int) -> None:
        self._payment_gateway.charge(total)
