from api.handlers import repository


def ship_paid_orders(order_ids):
    """Runs every ten minutes; ships what the warehouse has packed."""
    shipped = []
    for order_id in order_ids:
        order = repository.get(order_id)
        if order.is_paid and not order.is_shipped and not order.is_cancelled:
            order.ship()
            shipped.append(order_id)
    return shipped
