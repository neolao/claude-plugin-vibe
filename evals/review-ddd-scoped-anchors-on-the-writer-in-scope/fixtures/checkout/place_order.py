# Called by the checkout page once the customer confirms the basket.
from uuid import uuid4

from customers.customer import Customer
from orders.order import Line, Order
from orders.order_repository import OrderRepository


class PlaceOrder:
    def __init__(self, orders: OrderRepository):
        self._orders = orders

    def execute(self, customer: Customer, basket: list[Line]) -> Order:
        order = Order(str(uuid4()), customer.customer_id, customer.address)
        for line in basket:
            order.add_line(line.sku, line.qty, line.unit_price)
        self._orders.save(order)
        return order
