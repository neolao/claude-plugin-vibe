"""Discounts; called from checkout and from the monthly report."""


def discount_rate(customer, today):
    """Rate applied to a customer's order: 10% for loyal customers,
    doubled during the January sale."""
    rate = 0.10 if customer.loyal else 0.0
    if today.month == 1:
        rate *= 2
    return rate
