import smtplib

from invoicing.renderer import InvoiceRenderer


class InvoiceMailer:
    def __init__(self):
        self._renderer = InvoiceRenderer()
        self._smtp = smtplib.SMTP("mail.internal", 25)

    def send(self, customer, invoice):
        body = self._renderer.render(invoice)
        self._smtp.sendmail("billing@example.com", customer["email"], body)
