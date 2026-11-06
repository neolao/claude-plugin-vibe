"""Settlement check; called from the payment handler once a payment is recorded.

Amounts come from the payment provider's JSON as floats, in euros.
"""


def is_settled(invoice, payments):
    """True once the recorded payments cover the invoice total exactly."""
    return sum(p.amount for p in payments) == invoice.total


def outstanding(invoice, payments):
    return invoice.total - sum(p.amount for p in payments)
