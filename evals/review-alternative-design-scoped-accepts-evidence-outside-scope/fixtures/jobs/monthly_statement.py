from orders.report import OrderReport


def statement(order, customer, lines, period_end):
    """Runs on the first of the month for every customer with an order."""
    report = OrderReport(order.order_id, customer.name, lines, order.currency, customer.locale, "Monthly statement", period_end)
    return report.render()


def statement_copy(order, customer, lines, period_end):
    report = OrderReport(order.order_id, customer.name, lines, order.currency, customer.locale, "Monthly statement — copy", period_end)
    return report.render()
