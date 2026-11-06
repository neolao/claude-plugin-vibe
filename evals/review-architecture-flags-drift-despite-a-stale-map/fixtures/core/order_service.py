"""Places an order: prices it, stores it, confirms it. Called by the HTTP API."""

from core.discounts import discount_for
from core.ports import NotifierPort, OrderGatewayPort
from core.pricing import calculate_total
from notifications.templates import confirmation_subject


class OrderService:
    def __init__(self, gateway: OrderGatewayPort, notifier: NotifierPort) -> None:
        self._gateway = gateway
        self._notifier = notifier

    def place(self, order_id: str, line_amounts_cents: list[int], promo_code: str | None) -> int:
        discount = discount_for(promo_code, sum(line_amounts_cents))
        total = calculate_total(line_amounts_cents, discount)
        self._gateway.save(order_id, total)
        self._notifier.order_confirmed(order_id, total, confirmation_subject(order_id))
        return total
