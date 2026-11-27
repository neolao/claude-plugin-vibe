from billing.money import format_money
from billing.pricing import price_invoice
from notifications.channel import EmailChannel
from notifications.service import NotificationService


def send_invoice(customer, invoice):
    """Called by the nightly billing job for every invoice issued that day."""
    total = format_money(price_invoice(invoice), currency="EUR")
    service = NotificationService(EmailChannel(), retry_count=3)
    service.notify(customer["email"], f"Invoice {invoice['id']}: {total}")
