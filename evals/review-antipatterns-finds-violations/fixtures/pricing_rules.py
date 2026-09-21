def apply_discount(order, tier):
    # tier is a bare string compared everywhere — a new tier means editing
    # this if/elif chain instead of a closed set an enum or constant would
    # catch at the call site
    if tier == "gold":
        return order["total"] * 0.8
    elif tier == "silver":
        return order["total"] * 0.9
    elif tier == "bronze":
        return order["total"] * 0.95
    return order["total"]


class InvoiceFormatter:
    """Formats a Customer's invoice — but does it by reaching into the
    customer's own fields instead of asking the customer to format itself."""

    def format(self, customer):
        # every line here reads and combines *another* object's data; this
        # method has feature envy toward Customer
        lines = [customer.name, customer.address, customer.email]
        total = customer.balance_cents / 100  # money as a bare int of cents
        lines.append(f"Balance: {total} USD")
        return "\n".join(lines)
