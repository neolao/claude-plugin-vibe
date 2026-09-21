from logging_setup import log_charge


class PaymentGateway:
    """Charges a card through the payment processor."""

    def charge(self, order, *, retry: bool, notify: bool):
        log_charge(order)
        if retry:
            self._retry_charge(order)
        if notify:
            self._notify_customer(order)

    def _retry_charge(self, order):
        pass

    def _notify_customer(self, order):
        pass


def process_order(gateway, order):
    gateway.charge(order, retry=True, notify=False)
