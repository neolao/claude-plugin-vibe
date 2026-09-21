class Order:
    """An order placed by a user."""

    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items  # list of {"sku": str, "qty": int}
        self.status = "open"


def add_item(order, sku, qty):
    order.items.append({"sku": sku, "qty": qty})


def close_order(order):
    if len(order.items) > 50:
        raise ValueError("too many line items")
    order.status = "closed"
