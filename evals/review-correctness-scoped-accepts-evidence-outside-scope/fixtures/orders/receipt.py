"""Order receipts; called from the HTTP handlers once an order is placed."""


def receipt_recipient(order, customers):
    """E-mail address the receipt for this order goes to."""
    customer = customers.get(order.customer_id)
    return customer.email


def build_receipt(order, customers):
    return {
        "to": receipt_recipient(order, customers),
        "subject": f"Receipt for order {order.id}",
        "subtotal": order.subtotal,
    }
