"""Registry of the order handlers, filled by each handler module at import time."""

HANDLERS = {}


def register(name, handler):
    HANDLERS[name] = handler
