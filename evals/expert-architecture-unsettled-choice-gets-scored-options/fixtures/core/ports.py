from typing import Protocol

from core.message import Message


class Notifier(Protocol):
    def send(self, message: Message) -> str:
        """Delivers the message and returns the provider's delivery id."""
