"""Places an order: prices it for the customer's tier, stores it, confirms it."""

from adapters.smtp_notifier import NotifierPort
from core.ports.order_gateway import OrderGatewayPort
from core.pricing.policy import policy_for


class OrderService:
    def __init__(self, gateway: OrderGatewayPort, notifier: NotifierPort) -> None:
        self._gateway = gateway
        self._notifier = notifier

    def place(self, order_id: str, line_amounts_cents: list[int], customer_tier: str) -> int:
        total = policy_for(customer_tier).total(line_amounts_cents)
        self._gateway.save(order_id, total)
        self._notifier.order_confirmed(order_id, total)
        return total
