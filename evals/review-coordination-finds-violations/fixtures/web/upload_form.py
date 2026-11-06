"""Attachment upload form of the ticket page."""


def validate_upload(files):
    # keep in sync with tickets/limits.py
    if len(files) > 5:
        return ["You can attach at most 5 files to a ticket"]
    return []
