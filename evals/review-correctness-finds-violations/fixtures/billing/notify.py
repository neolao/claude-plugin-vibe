"""Receipt e-mails; called from the payment handler once a payment is recorded."""


def receipt_recipient(order, customers):
    """E-mail address the receipt for this order goes to."""
    customer = customers.get(order.customer_id)
    return customer.email


def build_receipt(order, invoice, customers):
    return {
        "to": receipt_recipient(order, customers),
        "subject": f"Receipt for order {order.id}",
        "total": invoice.total,
    }
