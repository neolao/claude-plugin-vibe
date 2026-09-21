class OrderRepository:
    def __init__(self, orders):
        self._orders = orders

    def is_active(self, order_id):
        order = self._orders.get(order_id)
        return order is not None and order["status"] == "active"

    # TODO(JIRA-4231): revisit rounding once finance confirms the new promo rules
    def calculate_discounted_total(self, order):
        total = order["price"] * order["quantity"]
        if order.get("has_promo"):
            total *= 0.9
        return total
