import asyncio


async def notify_partner(partner_client, order_id, payload):
    await partner_client.post(f"/orders/{order_id}", json=payload)


async def complete_order(partner_client, order_id, payload):
    """Called right after the order is finalized."""
    asyncio.create_task(notify_partner(partner_client, order_id, payload))
    return {"order_id": order_id, "status": "completed"}
