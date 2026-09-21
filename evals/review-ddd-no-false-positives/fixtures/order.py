class Order:
    """An aggregate root: enforces its own invariants and encapsulates its items."""

    MAX_LINE_ITEMS = 50

    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self._items = []
        self._status = "open"

    def add_item(self, sku, qty):
        if len(self._items) >= self.MAX_LINE_ITEMS:
            raise ValueError("too many line items")
        self._items.append({"sku": sku, "qty": qty})

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
