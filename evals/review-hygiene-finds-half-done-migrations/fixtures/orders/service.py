"""Order placement, called by the checkout handler in app.py."""
import settings
from payments.gateway import PaymentGateway


class OrderService:
    def __init__(self, repository):
        self.repository = repository
        self.payments = PaymentGateway(settings.PAYMENT_URL)

    def place(self, order):
        total = order.total_cents + order.shipping_cents
        self.payments.charge(order.customer_id, total)
        self.repository.save(order)
        return order.id
