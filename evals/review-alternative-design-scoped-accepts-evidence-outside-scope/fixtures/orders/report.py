from datetime import datetime


class OrderReport:
    """A printable view of one order. Built by the API handlers and the report jobs."""

    def __init__(self, order_id, customer_name, lines, currency, locale, footer, generated_at):
        self.order_id = order_id
        self.customer_name = customer_name
        self.lines = lines
        self.currency = currency
        self.locale = locale
        self.footer = footer
        self.generated_at = generated_at

    def total_cents(self):
        return sum(line["amount_cents"] for line in self.lines)

    def render(self):
        header = f"Order {self.order_id} for {self.customer_name}"
        body = "\n".join(
            f"{line['label']}: {line['amount_cents'] / 100:.2f} {self.currency}" for line in self.lines
        )
        stamp = self.generated_at.strftime("%Y-%m-%d")
        return f"{header}\n{body}\n{self.footer}\n{stamp}"
