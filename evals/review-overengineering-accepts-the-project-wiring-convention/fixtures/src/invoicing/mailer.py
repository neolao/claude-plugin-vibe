class InvoiceMailer:
    def __init__(self, renderer, sender):
        self._renderer = renderer
        self._sender = sender

    def send(self, customer, invoice):
        self._sender.send(customer["email"], self._renderer.render(invoice))
