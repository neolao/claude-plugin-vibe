"""Prices an order. Called from invoice_service once per invoice."""

VAT = 0.2


def total(order):
    net = sum(line.unit_price * line.quantity for line in order.lines)
    return round(net * (1 + VAT), 2)
