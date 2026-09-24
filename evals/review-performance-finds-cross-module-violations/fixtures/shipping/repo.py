async def shipments_for_customer(db, customer_id):
    return await db.fetch(
        "SELECT * FROM shipments WHERE customer_id = $1 ORDER BY created_at DESC",
        customer_id,
    )


async def shipment(db, shipment_id):
    return await db.fetchrow("SELECT * FROM shipments WHERE id = $1", shipment_id)


async def carrier(db, carrier_id):
    return await db.fetchrow("SELECT * FROM carriers WHERE id = $1", carrier_id)
