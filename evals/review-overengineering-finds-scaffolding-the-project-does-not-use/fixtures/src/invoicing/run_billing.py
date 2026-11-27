from invoicing.mailer import InvoiceMailer
from orders.sql_repository import SqlOrderRepository


def run_billing(db, day):
    """Entry point of the nightly billing job."""
    mailer = InvoiceMailer()
    repository = SqlOrderRepository(db)
    for order in repository.shipped_on(day):
        mailer.send(order["customer"], order["invoice"])
