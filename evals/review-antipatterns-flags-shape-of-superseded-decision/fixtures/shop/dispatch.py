"""Routes an order event to its handler. Called from the order views."""

from shop.handlers import HANDLERS


class Dispatcher:
    def __init__(self, handlers):
        self._handlers = handlers

    def dispatch(self, event_name, order):
        handler = self._handlers.get(event_name) or HANDLERS[event_name]
        handler(order)
