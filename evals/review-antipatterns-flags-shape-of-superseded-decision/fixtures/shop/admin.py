"""Operator console: enables and disables order handlers at runtime."""

from shop.handlers import HANDLERS, register


def disable_handler(name):
    HANDLERS.pop(name, None)


def enable_handler(name, handler):
    register(name, handler)
