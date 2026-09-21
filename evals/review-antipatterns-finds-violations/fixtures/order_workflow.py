"""Order lifecycle, driven by the checkout endpoint."""


class OrderWorkflow:
    def __init__(self):
        self.state = {}

    def init(self, order):
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
        if retry:
            pass
        if notify:
            pass

    def _ship(self, order):
        pass

    def _email_receipt(self, order):
        receipt_currency = "USD"
        return receipt_currency
