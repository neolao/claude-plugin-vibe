from notifications.service import NotificationService
from sms.sms_channel import SmsChannel


def send_payment_reminder(customer, invoice):
    """Called by the weekly dunning job for every overdue invoice."""
    service = NotificationService(SmsChannel(), retry_count=1)
    service.notify(customer["phone"], f"Invoice {invoice['id']} is overdue")
