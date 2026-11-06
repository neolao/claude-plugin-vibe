"""Ticket payload of API v2, the current contract."""

TICKET_FIELDS = ("reference", "status", "title", "priority", "due_at")


def serialize(ticket):
    return {field: getattr(ticket, field) for field in TICKET_FIELDS}
