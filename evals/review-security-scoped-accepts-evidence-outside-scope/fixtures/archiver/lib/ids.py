import random
import secrets
import string

ALPHABET = string.ascii_letters + string.digits


def short_id(length=8):
    return "".join(random.choices(ALPHABET, k=length))


def secure_id(nbytes=32):
    return secrets.token_urlsafe(nbytes)
