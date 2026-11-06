from datetime import datetime

from orders.report import OrderReport


def refund_lines(lines):
    return [dict(line, amount_cents=-line["amount_cents"]) for line in lines]


def ticket_summary(order, customer, lines):
    """Called by the support console when an agent opens a ticket."""
    report = OrderReport(order.order_id, customer.name, lines, "EUR", "en_GB", "Internal — support view", datetime.utcnow())
    return report.render()


def refund_preview(order, customer, lines):
    report = OrderReport(order.order_id, customer.name, refund_lines(lines), "EUR", "en_GB", "Refund preview", datetime.utcnow())
    return report.render()
