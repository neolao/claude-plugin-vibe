from dataclasses import dataclass

from customers.address import Address
from orders.money import Money

MAX_QTY_PER_LINE = 10


@dataclass(frozen=True)
class Line:
    sku: str
    qty: int
    unit_price: Money


class Order:
    def __init__(self, order_id: str, buyer_id: str, shipping_address: Address, status: str = "open"):
        self.order_id = order_id
        self.buyer_id = buyer_id
        self.shipping_address = shipping_address
        self._lines: list[Line] = []
        self._status = status

    def add_line(self, sku: str, qty: int, unit_price: Money) -> None:
        if qty < 1 or qty > MAX_QTY_PER_LINE:
            raise ValueError(f"qty must be between 1 and {MAX_QTY_PER_LINE}")
        self._lines.append(Line(sku, qty, unit_price))

    # Called from the account page when the buyer corrects the delivery street.
    def reroute(self, street: str) -> None:
        self.shipping_address.street = street

    def mark_paid(self) -> None:
        if self._status != "open":
            raise ValueError(f"order {self.order_id} is already {self._status}")
        self._status = "paid"

    @property
    def lines(self) -> tuple[Line, ...]:
        return tuple(self._lines)

    @property
    def status(self) -> str:
        return self._status

    def total(self) -> Money:
        total = Money(0, "EUR")
        for line in self._lines:
            total = total.plus(line.unit_price.times(line.qty))
        return total

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Order) and other.order_id == self.order_id

    def __hash__(self) -> int:
        return hash(self.order_id)
