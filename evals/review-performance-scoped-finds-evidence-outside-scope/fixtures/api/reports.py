async def monthly_volume(request, db):
    """GET /reports/monthly-volume — back-office dashboard, every active customer."""
    customers = await db.fetch("SELECT id FROM customers WHERE active")
    rows = []
    for customer in customers:
        count = await db.fetchval(
            "SELECT count(*) FROM shipments WHERE customer_id = $1"
            " AND created_at > now() - interval '30 days'",
            customer["id"],
        )
        rows.append({"customer_id": customer["id"], "shipments": count})
    return rows
