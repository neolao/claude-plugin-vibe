class OrderRepository:
    """Stores orders by id."""

    def __init__(self, orders_by_id):
        self._orders_by_id = orders_by_id

    def get(self, order_id):
        return self._orders_by_id[order_id]

    def save(self, order):
        self._orders_by_id[order.order_id] = order
