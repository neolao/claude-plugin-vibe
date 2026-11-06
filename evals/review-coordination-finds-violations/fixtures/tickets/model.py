"""Ticket model; called from the API views and the reports."""
from datetime import datetime


class Ticket:
    def __init__(self, reference, status, priority, due_at, attachments=()):
        self.reference = reference
        self.status = status
        self.priority = priority
        self.due_at = due_at
        self.attachments = list(attachments)


def is_overdue(ticket, now=None):
    now = now or datetime.utcnow()
    return ticket.status == "open" and ticket.due_at < now
