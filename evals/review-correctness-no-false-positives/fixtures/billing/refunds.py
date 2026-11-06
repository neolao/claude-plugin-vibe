"""Refund rules; called from the support console."""


def can_refund(order):
    """A refund is allowed for a paid order that has not shipped yet."""
    return order.status == "paid" and not order.shipped
