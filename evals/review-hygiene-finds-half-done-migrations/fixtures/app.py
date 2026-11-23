"""Entry point: builds the shared objects and maps routes to handlers."""
import settings
from billing.invoicer import Invoicer
from carriers.client import CarrierClient
from orders.repository import SqlOrderRepository
from orders.service import OrderService
from orders.shipping import shipping_cost
from support.refunds import RefundDesk

repository = SqlOrderRepository(settings.DATABASE_URL)
carrier = CarrierClient(settings.CARRIER_URL)
orders = OrderService(repository)
refunds = RefundDesk()


def handle_checkout(order):
    order.shipping_cents = shipping_cost(order, carrier)
    return orders.place(order)


def handle_invoice(order_id):
    return Invoicer(repository).invoice(order_id)


def handle_refund(customer_id, amount_cents):
    return refunds.refund(customer_id, amount_cents)


ROUTES = {
    "POST /checkout": handle_checkout,
    "GET /invoices/<order_id>": handle_invoice,
    "POST /refunds": handle_refund,
}
