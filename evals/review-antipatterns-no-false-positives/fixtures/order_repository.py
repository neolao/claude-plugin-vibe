from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class Money:
    cents: int
    currency: str = "USD"

    def __add__(self, other):
        if other.currency != self.currency:
            raise ValueError("currency mismatch")
        return Money(self.cents + other.cents, self.currency)


MAX_RETRIES = 3


class OrderRepository:
    """Persists and retrieves Order aggregates."""

    def __init__(self, connection):
        self._connection = connection

    def save(self, order):
        row = {
            "id": order.id,
            "total_cents": order.total.cents,
            "status": order.status.value,
        }
        self._connection.execute("orders", row)

    def find(self, order_id):
        return self._connection.fetch(order_id)

    def parse_placed_at(self, value):
        return datetime.fromisoformat(value)
