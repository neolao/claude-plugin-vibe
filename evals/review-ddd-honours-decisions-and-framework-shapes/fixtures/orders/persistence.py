# The row shape of the `orders` table, as the repository reads and writes it.
from dataclasses import dataclass


@dataclass
class OrderRow:
    id: str
    customer_id: str
    status: str


@dataclass
class OrderLineRow:
    order_id: str
    sku: str
    qty: int
    unit_cents: int
