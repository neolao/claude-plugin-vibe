class EventBus:
    def __init__(self):
        self._handlers = []

    def subscribe(self, handler):
        self._handlers.append(handler)

    def publish(self, e):
        for handler in self._handlers:
            handler(e)
