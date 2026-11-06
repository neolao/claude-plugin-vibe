from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    channel: str
    recipient: str
    body: str
