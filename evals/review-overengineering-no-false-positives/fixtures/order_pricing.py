from decimal import Decimal


class OrderRepository:
    """Reads orders from the Postgres `orders` table."""

    def __init__(self, db):
        self._db = db

    def find(self, order_id):
        row = self._db.fetch_one(
            "SELECT price, quantity, discount_rate, tax_rate, free_shipping"
            " FROM orders WHERE id = %s",
            (order_id,),
        )
        if row is None:
            return None
        price, quantity, discount_rate, tax_rate, free_shipping = row
        return {
            "price": Decimal(price),
            "quantity": quantity,
            "discount_rate": Decimal(discount_rate or 0),
            "tax_rate": Decimal(tax_rate or 0),
            "free_shipping": bool(free_shipping),
        }


class OrderPricingService:
    """Owns the tax, discount, and shipping rules, which the pricing team
    changes weekly."""

    SHIPPING_FEE = Decimal("5.99")

    def price(self, order):
        subtotal = order["price"] * order["quantity"]
        subtotal *= 1 - order["discount_rate"]
        subtotal += self._shipping_cost(order)
        return (subtotal * (1 + order["tax_rate"])).quantize(Decimal("0.01"))

    def _shipping_cost(self, order):
        return Decimal(0) if order["free_shipping"] else self.SHIPPING_FEE


class OrderController:
    """Called from the HTTP router for GET /orders/<id>/price."""

    def __init__(self, repository, pricing_service):
        self._repository = repository
        self._pricing_service = pricing_service

    def handle_price_request(self, request):
        order_id = request.params.get("order_id", "")
        if not order_id.isdigit():
            return {"status": 400, "error": "order_id must be numeric"}
        order = self._repository.find(int(order_id))
        if order is None:
            return {"status": 404, "error": "order not found"}
        return {"status": 200, "total": str(self._pricing_service.price(order))}
