from adapters.postgres.order_repository import PostgresOrderRepository
from core.services.place_order import PlaceOrder
from invoicing.mailer import InvoiceMailer
from invoicing.renderer import InvoiceRenderer
from invoicing.smtp_sender import SmtpSender


class App:
    def __init__(self, place_order, invoice_mailer):
        self.place_order = place_order
        self.invoice_mailer = invoice_mailer


def build_app(db, smtp_host):
    """Composition root, called once by main."""
    repository = PostgresOrderRepository(db)
    sender = SmtpSender(smtp_host)
    mailer = InvoiceMailer(InvoiceRenderer(), sender)
    return App(PlaceOrder(repository), mailer)
