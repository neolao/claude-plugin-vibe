"""Amount helpers shared by the billing commands."""


def subtotal_cents(lines):
    return sum(line["unit_cents"] * line["qty"] for line in lines)


def format_amount(cents):
    return f"{cents / 100:.2f} EUR"
