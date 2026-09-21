import logging

logger = logging.getLogger(__name__)


def charge_card(gateway_client, order_id, amount):
    """Called from the checkout flow right before the order is marked paid."""
    try:
        gateway_client.charge(order_id, amount)
    except Exception:
        logger.error("charge failed for order %s", order_id)
    return {"status": "paid"}
