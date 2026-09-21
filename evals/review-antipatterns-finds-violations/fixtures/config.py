"""Process-wide configuration and the handler registry."""

_REGISTRY = {}


def register(name, handler):
    _REGISTRY[name] = handler


def unregister(name):
    del _REGISTRY[name]


REDIS_POOL_SIZE = 50
REDIS_SOCKET_TIMEOUT = 30
REDIS_RETRY_ON_TIMEOUT = True
