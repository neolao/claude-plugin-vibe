from orders.repository import OrderRepository

repository = OrderRepository()


def can_cancel(order):
    """Called by the customer account page to show or hide the Cancel button."""
    return not order.is_shipped and not order.is_cancelled and not order.is_refunded


def can_refund(order):
    """Called by the support console to enable the Refund action."""
    return order.is_paid and not order.is_refunded and (order.is_cancelled or order.is_shipped)


def post_cancel(order_id):
    order = repository.get(order_id)
    if not can_cancel(order):
        return {"status": 409, "error": "cannot cancel"}
    order.cancel()
    return {"status": 200, "state": order.status_label()}


def post_refund(order_id):
    order = repository.get(order_id)
    if not can_refund(order):
        return {"status": 409, "error": "cannot refund"}
    order.refund()
    return {"status": 200, "state": order.status_label()}


def get_order(order_id):
    order = repository.get(order_id)
    return {
        "status": 200,
        "state": order.status_label(),
        "actions": {
            "cancel": can_cancel(order),
            "refund": can_refund(order),
        },
    }
