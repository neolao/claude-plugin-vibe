from vendor_push import PushGateway

from core.message import Message


class PushNotifier:
    def __init__(self, gateway: PushGateway):
        self.gateway = gateway

    @classmethod
    def from_env(cls):
        return cls(PushGateway.from_env())

    def send(self, message: Message) -> str:
        return self.gateway.notify(device=message.recipient, text=message.body)
