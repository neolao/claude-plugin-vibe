from dataclasses import dataclass

from money import Money

MAX_QTY_PER_LINE = 10


@dataclass(frozen=True)
class Line:
    sku: str
    qty: int
    unit_price: Money


class Cart:
    def __init__(self, cart_id: str, customer_id: str):
        self.cart_id = cart_id
        self.customer_id = customer_id
        self._lines: list[Line] = []

    def add_line(self, sku: str, qty: int, unit_price: Money) -> None:
        if qty < 1 or qty > MAX_QTY_PER_LINE:
            raise ValueError(f"qty must be between 1 and {MAX_QTY_PER_LINE}")
        self._lines.append(Line(sku, qty, unit_price))

    @property
    def lines(self) -> tuple[Line, ...]:
        return tuple(self._lines)

    def total(self) -> Money:
        total = Money(0, "EUR")
        for line in self._lines:
            total = total.plus(line.unit_price.times(line.qty))
        return total

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Cart) and other.cart_id == self.cart_id

    def __hash__(self) -> int:
        return hash(self.cart_id)
