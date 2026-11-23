"""Invoice documents, built per request by the invoice handler in app.py."""
from billing.pdf import PdfRenderer


class Invoicer:
    def __init__(self, repository):
        self.repository = repository
        # PdfRenderer keeps the lines of the document it is drawing, and the
        # objects app.py builds at start-up are shared by every request
        # thread: a shared renderer would mix two invoices' lines.
        self.renderer = PdfRenderer()

    def invoice(self, order_id):
        order = self.repository.get(order_id)
        return self.renderer.render(
            f"Invoice {order.id}",
            [f"Customer: {order.customer_id}", f"Total: {order.total_cents} cents"],
        )
