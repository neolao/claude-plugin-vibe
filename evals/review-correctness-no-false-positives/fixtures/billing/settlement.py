"""Settlement check; called from the payment handler once a payment is recorded.

Amounts come from the payment provider's JSON as floats, in euros.
"""
import math

HALF_CENT = 0.005


def is_settled(invoice, payments):
    """True once the recorded payments cover the invoice total, to the cent."""
    return math.isclose(sum(p.amount for p in payments), invoice.total, abs_tol=HALF_CENT)


def outstanding(invoice, payments):
    return invoice.total - sum(p.amount for p in payments)
