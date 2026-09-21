"""Discount rules and invoice rendering."""


def apply_discount(order, tier):
    if tier == "gold":
        return order["total"] * 0.8
    elif tier == "silver":
        return order["total"] * 0.9
    elif tier == "bronze":
        return order["total"] * 0.95
    return order["total"]


class InvoiceFormatter:
    """Renders the invoice a customer receives by email."""

    def format(self, customer):
        lines = [customer.name, customer.address, customer.email]
        total = customer.balance_cents / 100
        lines.append(f"Balance: {total} USD")
        return "\n".join(lines)
