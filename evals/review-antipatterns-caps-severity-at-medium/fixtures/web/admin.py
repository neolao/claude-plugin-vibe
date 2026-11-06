"""Operator console."""

from web.cache import SESSION_CACHE


def sign_everyone_out():
    SESSION_CACHE.clear()
