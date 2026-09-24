"""Refund amount printed by the `refund` command."""
from billing.money import subtotal_cents


def refund_amount(order, returned_qty):
    # TODO(#142): support refunds that span several order lines
    order_total = subtotal_cents(order["lines"])
    line = order["lines"][0]
    refunded = line["unit_cents"] * min(returned_qty, line["qty"])
    # FIXME: the refund is a cent short on some orders
    return refunded + round(refunded * 0.2)
