import asyncio
import logging

logger = logging.getLogger(__name__)


async def notify_partner(partner_client, order_id, payload):
    try:
        await partner_client.post(f"/orders/{order_id}", json=payload)
    except Exception:
        logger.exception("partner notification failed for order %s", order_id)


async def complete_order(partner_client, order_id, payload):
    """Notifying the partner is intentionally fire-and-forget: the order is
    already committed and the partner webhook is not on the critical path."""
    task = asyncio.create_task(notify_partner(partner_client, order_id, payload))
    task.add_done_callback(lambda t: t.exception())
    return {"order_id": order_id, "status": "completed"}
