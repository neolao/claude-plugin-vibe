from logging_setup import log_charge


class PaymentGateway:
    """Charges a card through the processor. Retries and notifications are
    explicit keyword arguments — a call site reads its own intent."""

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
    # keyword arguments make each flag's meaning obvious at the call site
    gateway.charge(order, retry=True, notify=False)
