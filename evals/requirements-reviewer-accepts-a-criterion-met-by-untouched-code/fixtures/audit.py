"""Audit log. Every recorded event is kept in order for the compliance export."""

EVENTS = []


def record(event, **fields):
    EVENTS.append({"event": event, **fields})
