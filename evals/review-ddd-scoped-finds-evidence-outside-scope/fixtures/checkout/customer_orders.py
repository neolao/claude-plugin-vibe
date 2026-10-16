# Called by the account page to list a customer's past orders.
from orders.order import Order
from orders.order_repository import OrderRepository


class CustomerOrders:
    def __init__(self, orders: OrderRepository):
        self._orders = orders

    def for_customer(self, customer_id: str) -> list[Order]:
        return self._orders.find_for_buyer(customer_id)
