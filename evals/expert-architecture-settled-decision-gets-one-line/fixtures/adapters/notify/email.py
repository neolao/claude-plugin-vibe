from core.notification_router import register
from vendor_mail import MailClient

client = MailClient.from_env()


@register("email")
def send(message):
    return client.send(to=message.recipient, text=message.body)
