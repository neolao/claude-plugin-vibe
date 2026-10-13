import logging
from datetime import datetime, timezone

from core.pricing import calculate_total

log = logging.getLogger(__name__)


class OrderService:
    """Places an order: prices it, persists it, then notifies the customer."""

    def __init__(self, gateway, notifier):
        self._gateway = gateway
        self._notifier = notifier

    def place_order(self, order):
        total = calculate_total(order)
        self._gateway.save(order["id"], total)
        self._notifier.order_confirmed(order["id"], total)
        log.info("order %s placed at %s", order["id"], datetime.now(timezone.utc).isoformat())
        return total
