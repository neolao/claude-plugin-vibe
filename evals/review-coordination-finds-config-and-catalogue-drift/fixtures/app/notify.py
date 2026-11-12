"""Builds the e-mail text sent after an order event."""
from i18n.messages import MESSAGES


def text_for(event, ref):
    return MESSAGES[f"order.{event}"].format(ref=ref)


def after_refund(ref):
    return MESSAGES["order.refunded"].format(ref=ref)
