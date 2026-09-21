class OrderRepository:
    def __init__(self, db):
        self._db = db

    def find(self, order_id):
        return self._db.query("orders", order_id)


class OrderPricingService:
    """Owns the tax, discount, and shipping rules - kept separate from
    persistence and the request-handling layer because the pricing rules
    change weekly while the repository and controller do not."""

    def price(self, order):
        subtotal = order["price"] * order["quantity"]
        subtotal *= 1 - order.get("discount_rate", 0)
        subtotal += self._shipping_cost(order)
        return subtotal * (1 + order.get("tax_rate", 0))

    def _shipping_cost(self, order):
        return 0 if order.get("free_shipping") else 5.99


class OrderController:
    def __init__(self, repository, pricing_service):
        self._repository = repository
        self._pricing_service = pricing_service

    def handle_price_request(self, order_id):
        order = self._repository.find(order_id)
        return self._pricing_service.price(order)
