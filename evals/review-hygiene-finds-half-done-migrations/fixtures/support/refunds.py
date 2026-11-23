"""Refunds issued by the support team, called by the refund handler in app.py."""
import settings
from payments.gateway import PaymentGateway


class RefundDesk:
    def __init__(self):
        self.gateway = PaymentGateway(settings.PAYMENT_URL)

    def refund(self, customer_id, amount_cents):
        return self.gateway.refund(customer_id, amount_cents)
