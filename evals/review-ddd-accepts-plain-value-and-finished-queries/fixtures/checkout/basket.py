# Called by the checkout page once the customer confirms the basket.
from datetime import date
from uuid import uuid4

from catalog.product import CATALOG
from orders.order import Order


def place_order(customer_id: str, basket: dict[str, int], today: date) -> Order:
    order = Order(str(uuid4()), customer_id, today)
    for sku, qty in basket.items():
        product = CATALOG[sku]
        order.add_line(product.sku, qty, product.price)
    return order
