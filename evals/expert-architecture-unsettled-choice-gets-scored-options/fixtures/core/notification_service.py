"""Sends a message through the channel it names. Called from app.py once per notification."""

from core.message import Message
from core.ports import Notifier


class NotificationService:
    def __init__(self, email: Notifier, push: Notifier):
        self.email = email
        self.push = push

    def send(self, message: Message) -> str:
        if message.channel == "email":
            return self.email.send(message)
        elif message.channel == "push":
            return self.push.send(message)
        raise ValueError(f"unknown channel: {message.channel}")
