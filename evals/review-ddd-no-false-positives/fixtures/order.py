from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    sku: str
    qty: int


class Order:
    """An order placed by a customer."""

    MAX_LINE_ITEMS = 50

    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self._items = []
        self._status = "open"

    def add_item(self, sku, qty):
        if len(self._items) >= self.MAX_LINE_ITEMS:
            raise ValueError("too many line items")
        self._items.append(LineItem(sku, qty))

    def close(self):
        if not self._items:
            raise ValueError("cannot close an empty order")
        self._status = "closed"

    @property
    def items(self):
        return tuple(self._items)

    @property
    def status(self):
        return self._status

    def __eq__(self, other):
        return isinstance(other, Order) and other.order_id == self.order_id

    def __hash__(self):
        return hash(self.order_id)
