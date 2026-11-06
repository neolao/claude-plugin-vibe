"""Signs a user out."""

from web.cache import SESSION_CACHE


def logout(token):
    SESSION_CACHE.pop(token, None)
