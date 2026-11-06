"""Billing periods; called from the invoice generator."""


def months_in(first, last):
    """The month numbers from first to last, both included (1..12)."""
    return list(range(first, last))


def period_label(first, last):
    months = months_in(first, last)
    return f"{months[0]:02d}-{months[-1]:02d}"
