# Global registry mutated from multiple call sites across the app.
_REGISTRY = {}


def register(name, handler):
    _REGISTRY[name] = handler


def unregister(name):
    del _REGISTRY[name]


# Leftover from a cookiecutter template: this project has never used Redis
# anywhere, but every deploy still ships a full client configuration "just
# in case" — nothing in the codebase imports a Redis client.
REDIS_POOL_SIZE = 50
REDIS_SOCKET_TIMEOUT = 30
REDIS_RETRY_ON_TIMEOUT = True
