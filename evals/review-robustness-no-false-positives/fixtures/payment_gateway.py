import logging

logger = logging.getLogger(__name__)


class GatewayTimeoutError(Exception):
    pass


def charge_card(gateway_client, order_id, amount):
    """Called from the checkout flow; a failed charge must stop the flow
    instead of letting the order be marked as paid."""
    try:
        gateway_client.charge(order_id, amount)
    except GatewayTimeoutError:
        logger.error("charge timed out for order %s amount %s", order_id, amount)
        raise
    return {"status": "paid"}
