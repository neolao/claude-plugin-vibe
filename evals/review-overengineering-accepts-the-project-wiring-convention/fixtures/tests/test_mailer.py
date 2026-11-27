from invoicing.mailer import InvoiceMailer
from invoicing.renderer import InvoiceRenderer


class RecordingSender:
    def __init__(self):
        self.sent = []

    def send(self, recipient, body):
        self.sent.append((recipient, body))


def test_mailer_sends_rendered_invoice_to_customer():
    sender = RecordingSender()
    mailer = InvoiceMailer(InvoiceRenderer(), sender)
    mailer.send({"email": "ada@example.com"}, {"id": 7, "lines": [{"label": "Seat", "amount": 12}]})
    assert sender.sent == [("ada@example.com", "Invoice 7\nSeat: 12.00")]
