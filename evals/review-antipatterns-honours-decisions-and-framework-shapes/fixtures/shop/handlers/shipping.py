"""Ships an order once it is paid."""

from shop.handlers import register


def handle(order):
    order.mark_shipped()


register("shipping", handle)
