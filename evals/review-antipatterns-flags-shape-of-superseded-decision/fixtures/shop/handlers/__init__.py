"""The order handlers."""

HANDLERS = {}


def register(name, handler):
    HANDLERS[name] = handler
