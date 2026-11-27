class PlaceOrder:
    def __init__(self, repository):
        self._repository = repository

    def __call__(self, order):
        if not order["lines"]:
            raise ValueError("an order needs at least one line")
        order["status"] = "placed"
        self._repository.add(order)
        return order["id"]
