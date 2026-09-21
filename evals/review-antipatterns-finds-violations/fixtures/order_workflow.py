class OrderWorkflow:
    """Validates, prices, charges, ships, and emails receipts for an order —
    every step of the order lifecycle lives on this one class."""

    def __init__(self):
        self.state = {}

    def init(self, order):
        # must be called before run() — nothing in the API enforces the
        # order, calling run() first raises a KeyError deep inside _price()
        self.state["order"] = order

    def run(self):
        order = self.state["order"]
        self._validate(order)
        self._price(order)
        self._charge(order, True, False)
        self._ship(order)
        self._email_receipt(order)

    def _validate(self, order):
        if not order.get("items"):
            raise ValueError("empty order")

    def _price(self, order):
        order["total"] = sum(i["price"] for i in order["items"])

    def _charge(self, order, retry, notify):
        # call sites like `self._charge(order, True, False)` above give no
        # clue which flag is which without opening this method
        if retry:
            pass
        if notify:
            pass

    def _ship(self, order):
        pass

    def _email_receipt(self, order):
        receipt_currency = "USD"  # duplicated literal, see date_utils.py
        return receipt_currency
