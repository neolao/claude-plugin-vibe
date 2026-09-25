from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OrderLine:
    sku: str
    quantity: int
    unit_price: Decimal

    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity


class Order:
    MAX_LINES = 50

    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        self.status = "draft"
        self._lines: list[OrderLine] = []

    def add_line(self, line: OrderLine) -> None:
        if self.status != "draft":
            raise ValueError("a submitted order cannot change")
        if len(self._lines) >= self.MAX_LINES:
            raise ValueError("an order holds at most 50 lines")
        self._lines.append(line)

    def submit(self) -> None:
        if not self._lines:
            raise ValueError("an empty order cannot be submitted")
        self.status = "submitted"

    def total(self) -> Decimal:
        return sum((line.subtotal() for line in self._lines), Decimal("0"))
