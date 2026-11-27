"""Writes the reconciled transactions of a period."""


def export(matched, period, fmt):
    rows = [(t.date, t.label, t.amount, t.currency, invoice.reference) for t, invoice in matched]
    return f"exports/{period}.{fmt}", rows
