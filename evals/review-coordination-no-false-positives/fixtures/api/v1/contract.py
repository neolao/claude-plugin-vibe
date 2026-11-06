"""Ticket payload of API v1. Frozen since 2025-06: the integrations still on v1 rely on this exact shape."""

TICKET_FIELDS = ("reference", "status", "title")


def serialize(ticket):
    return {field: getattr(ticket, field) for field in TICKET_FIELDS}
