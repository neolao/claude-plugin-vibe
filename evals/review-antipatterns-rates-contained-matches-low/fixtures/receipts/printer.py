"""Renders a receipt as plain text for the thermal printer."""


class ReceiptPrinter:
    def print_receipt(self, receipt):
        body = "\n".join(f"{line.label}: {line.amount.cents / 100:.2f}" for line in receipt.lines)
        return self._render(body, True)

    def _render(self, text, uppercase):
        return text.upper() if uppercase else text
