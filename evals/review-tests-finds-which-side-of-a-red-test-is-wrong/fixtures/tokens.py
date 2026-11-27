"""Expiring access tokens handed to the mobile app."""
from dataclasses import dataclass
from datetime import date


@dataclass
class Token:
    value: str
    expires: date


def is_expired(token):
    """True once the token's expiry day has passed."""
    return token.expires < date.today()
