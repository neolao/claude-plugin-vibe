from vendor_mail import MailClient

from core.message import Message


class EmailNotifier:
    def __init__(self, client: MailClient):
        self.client = client

    @classmethod
    def from_env(cls):
        return cls(MailClient.from_env())

    def send(self, message: Message) -> str:
        return self.client.send(to=message.recipient, text=message.body)
