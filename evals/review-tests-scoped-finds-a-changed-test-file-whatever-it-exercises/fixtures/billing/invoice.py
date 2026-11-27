"""Monthly invoice totals."""


def invoice_total(lines):
    """Sum of quantity times unit price over the invoice lines."""
    if not lines:
        raise ValueError("empty invoice")
    return sum(quantity * unit_price for quantity, unit_price in lines)
