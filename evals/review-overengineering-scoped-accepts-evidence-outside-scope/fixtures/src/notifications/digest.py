from billing.money import format_money


def build_daily_digest(customer, invoices):
    """Called once a day per customer with the invoices issued since the last digest."""
    total = sum(invoice["total"] for invoice in invoices)
    lines = [f"- {invoice['id']}: {format_money(invoice['total'], currency='EUR')}" for invoice in invoices]
    header = f"Hello {customer['name']}, {len(invoices)} invoice(s) today, {format_money(total, currency='EUR')} in total"
    return "\n".join([header, *lines])
