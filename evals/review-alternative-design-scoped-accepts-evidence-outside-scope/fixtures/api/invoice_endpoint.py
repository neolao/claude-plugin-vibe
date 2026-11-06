from datetime import datetime

from orders.report import OrderReport


def legal_footer(customer):
    return f"{customer.legal_name} — VAT {customer.vat_number}"


def negate(lines):
    return [dict(line, amount_cents=-line["amount_cents"]) for line in lines]


def invoice(order, customer, lines):
    """Called by the accounting integration once per issued invoice."""
    report = OrderReport(order.order_id, customer.legal_name, lines, order.currency, customer.locale, legal_footer(customer), datetime.utcnow())
    return report.render()


def credit_note(order, customer, lines):
    report = OrderReport(order.order_id, customer.legal_name, negate(lines), order.currency, customer.locale, legal_footer(customer), datetime.utcnow())
    return report.render()
