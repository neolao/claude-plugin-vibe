import asyncio
import logging

logger = logging.getLogger(__name__)

_background_tasks = set()


async def notify_partner(partner_client, order_id, payload):
    try:
        await asyncio.wait_for(
            partner_client.post(f"/orders/{order_id}", json=payload), timeout=10
        )
    except Exception:
        logger.exception("partner notification failed for order %s", order_id)


def _forget(task):
    _background_tasks.discard(task)
    if not task.cancelled():
        task.exception()


async def complete_order(partner_client, order_id, payload):
    """Notifying the partner is intentionally fire-and-forget: the order is
    already committed and the partner webhook is not on the critical path."""
    task = asyncio.create_task(notify_partner(partner_client, order_id, payload))
    _background_tasks.add(task)
    task.add_done_callback(_forget)
    return {"order_id": order_id, "status": "completed"}
