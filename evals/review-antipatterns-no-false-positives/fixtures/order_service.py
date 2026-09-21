class OrderService:
    """Places an order in one call — no setup method required, so there is
    no ordering for callers to get wrong."""

    def __init__(self, repository, gateway):
        self._repository = repository
        self._gateway = gateway

    def place_order(self, order):
        # everything the method needs comes in through this one call;
        # nothing must run before it in a particular order
        self._gateway.charge(order, retry=True, notify=False)
        self._repository.save(order)


# The currency code lives in one place (Money's default in
# order_repository.py) and every caller gets it from there — nothing
# duplicates the literal "USD".
