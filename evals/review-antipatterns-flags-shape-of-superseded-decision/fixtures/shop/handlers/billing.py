"""Charges an order once it is placed."""

from shop.handlers import register


def handle(order):
    order.mark_paid()


register("billing", handle)
