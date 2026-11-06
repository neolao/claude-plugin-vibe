from orders.report import OrderReport


def taxable(lines):
    return [line for line in lines if line.get("taxable", True)]


def tax_line(order, customer, lines, quarter_end):
    """Runs quarterly for the tax filing."""
    report = OrderReport(order.order_id, customer.legal_name, taxable(lines), order.currency, "en_GB", "Tax export", quarter_end)
    return report.render()


def tax_correction(order, customer, lines, quarter_end):
    report = OrderReport(order.order_id, customer.legal_name, taxable(lines), order.currency, "en_GB", "Tax correction", quarter_end)
    return report.render()
