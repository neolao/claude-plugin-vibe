from core.pricing import calculate_total


class OrderService:
    """Places an order: prices it and hands the total to whatever gateway
    was injected — core never picks or builds its own adapter."""

    def __init__(self, gateway):
        self._gateway = gateway

    def place_order(self, order):
        total = calculate_total(order)
        self._gateway.save(order["id"], total)
        return total
