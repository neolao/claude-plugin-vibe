"""Routes a message to the channel it names. Called from the HTTP layer once per notification."""

from core.message import Message

CHANNELS = {}


def register(name):
    def decorator(send):
        CHANNELS[name] = send
        return send

    return decorator


def dispatch(message: Message):
    try:
        send = CHANNELS[message.channel]
    except KeyError:
        raise ValueError(f"unknown channel: {message.channel}")
    return send(message)
