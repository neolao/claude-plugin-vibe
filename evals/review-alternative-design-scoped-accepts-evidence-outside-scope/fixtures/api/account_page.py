from datetime import datetime

from orders.report import OrderReport


def order_view(order, customer, lines):
    """Called when the customer opens an order on their account page."""
    report = OrderReport(order.order_id, customer.name, lines, "EUR", customer.locale, "Thank you for your order", datetime.utcnow())
    return report.render()


def order_download(order, customer, lines):
    report = OrderReport(order.order_id, customer.name, lines, "EUR", customer.locale, "Printed from your account", datetime.utcnow())
    return report.render()
