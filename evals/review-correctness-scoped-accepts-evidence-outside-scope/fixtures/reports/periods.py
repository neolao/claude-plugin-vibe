"""Reporting periods; called from the monthly summary."""


def months_in(first, last):
    """The month numbers from first to last, both included (1..12)."""
    return list(range(first, last))
