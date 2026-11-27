from notifications.channel import EmailChannel
from notifications.service import NotificationService


def send_payment_reminder(customer, invoice):
    """Called by the weekly dunning job for every overdue invoice."""
    service = NotificationService(EmailChannel(), retry_count=3)
    service.notify(customer["email"], f"Invoice {invoice['id']} is overdue")
