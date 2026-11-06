"""Signs a user in."""

from web.cache import SESSION_CACHE


def login(user, token):
    SESSION_CACHE[token] = user
