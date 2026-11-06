from orders.report import OrderReport


def digest_entry(order, customer, lines, run_date):
    """Runs every night for the operations mailbox."""
    report = OrderReport(order.order_id, customer.name, lines, "EUR", "en_GB", "Daily digest", run_date)
    return report.render()


def digest_exception(order, customer, lines, run_date):
    report = OrderReport(order.order_id, customer.name, lines, "EUR", "en_GB", "Needs attention", run_date)
    return report.render()
