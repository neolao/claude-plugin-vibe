"""Invoice text printed by the `invoice` command."""
from billing.money import subtotal_cents


def render_invoice(order):
    subtotal = subtotal_cents(order["lines"])
    vat = round(subtotal * 0.2)
    return "\n".join(
        [
            f"Invoice for {order['customer']}",
            f"Subtotal: {_money(subtotal)}",
            f"VAT: {_money(vat)}",
            f"Total: {_money(subtotal + vat)}",
        ]
    )


def _money(cents):
    return "%.2f EUR" % (cents / 100)
