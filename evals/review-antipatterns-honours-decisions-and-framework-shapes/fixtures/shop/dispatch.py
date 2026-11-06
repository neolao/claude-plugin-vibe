"""Routes an order event to its handler. Called from the order views."""

import shop.handlers.billing  # noqa: F401  registers at import
import shop.handlers.shipping  # noqa: F401  registers at import
from shop.handlers import HANDLERS


def dispatch(event_name, order):
    handler = HANDLERS[event_name]
    handler(order)
