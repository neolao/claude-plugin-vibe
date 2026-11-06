from .order import Order


class OrderRepository:
    """In-memory store used by the API handlers and the warehouse job."""

    def __init__(self):
        self._orders = {}

    def add(self, order):
        self._orders[order.order_id] = order

    def get(self, order_id):
        return self._orders[order_id]

    def to_row(self, order):
        return {
            "id": order.order_id,
            "total_cents": order.total_cents,
            "is_paid": order.is_paid,
            "is_shipped": order.is_shipped,
            "is_cancelled": order.is_cancelled,
            "is_refunded": order.is_refunded,
        }

    def from_row(self, row):
        order = Order(row["id"], row["total_cents"])
        order.is_paid = row["is_paid"]
        order.is_shipped = row["is_shipped"]
        order.is_cancelled = row["is_cancelled"]
        order.is_refunded = row["is_refunded"]
        return order
