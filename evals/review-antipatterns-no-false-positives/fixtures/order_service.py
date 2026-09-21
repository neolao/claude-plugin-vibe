class OrderService:
    """Places an order: charges it, then persists it."""

    def __init__(self, repository, gateway):
        self._repository = repository
        self._gateway = gateway

    def place_order(self, order):
        self._gateway.charge(order, retry=True, notify=False)
        self._repository.save(order)
