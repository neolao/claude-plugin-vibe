"""Limits applied when a ticket is created or updated."""

MAX_ATTACHMENTS = 5
MAX_TITLE_LENGTH = 120


def check_attachments(ticket):
    if len(ticket.attachments) > MAX_ATTACHMENTS:
        raise ValueError(f"{ticket.reference}: at most {MAX_ATTACHMENTS} attachments")
