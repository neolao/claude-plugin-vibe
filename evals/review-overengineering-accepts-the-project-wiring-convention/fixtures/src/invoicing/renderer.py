class InvoiceRenderer:
    def render(self, invoice):
        lines = [f"{line['label']}: {line['amount']:.2f}" for line in invoice["lines"]]
        return "\n".join([f"Invoice {invoice['id']}", *lines])
