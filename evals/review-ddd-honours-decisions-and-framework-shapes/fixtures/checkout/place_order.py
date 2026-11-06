# Called by the checkout page once the customer confirms the basket.
from uuid import uuid4

from inventory.reservation import StockReservation
from orders.events import OrderPlaced
from orders.order import Line, Order
from orders.order_repository import OrderRepository


class PlaceOrder:
    def __init__(self, orders: OrderRepository, reservation: StockReservation):
        self._orders = orders
        self._reservation = reservation

    def execute(self, customer_id: str, basket: list[Line]) -> Order:
        order = Order(str(uuid4()), customer_id)
        for line in basket:
            order.add_line(line.sku, line.qty, line.unit_price)
        self._orders.save(order)
        self._reservation.on_order_placed(
            OrderPlaced(order.order_id, order.customer_id, tuple(l.sku for l in order.lines))
        )
        return order
