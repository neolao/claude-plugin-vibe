from core.notification_router import register
from vendor_push import PushGateway

gateway = PushGateway.from_env()


@register("push")
def send(message):
    return gateway.notify(device=message.recipient, text=message.body)
