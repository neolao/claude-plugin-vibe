"""Imports every channel module so each one registers itself at startup."""

from adapters.notify import email, push  # noqa: F401
