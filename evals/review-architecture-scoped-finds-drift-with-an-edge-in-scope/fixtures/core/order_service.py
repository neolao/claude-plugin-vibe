"""Places an order: prices it, stores it, confirms it, raises the event."""

from core.events import OrderPlaced
from core.ports import NotifierPort, OrderGatewayPort
from core.pricing import calculate_total


class OrderService:
    def __init__(self, gateway: OrderGatewayPort, notifier: NotifierPort) -> None:
        self._gateway = gateway
        self._notifier = notifier

    def place(self, order_id: str, line_amounts_cents: list[int]) -> int:
        total = calculate_total(line_amounts_cents)
        self._gateway.save(order_id, total)
        self._notifier.order_confirmed(order_id, total)
        OrderPlaced(order_id, total).publish()
        return total
