from shipping import repo


async def describe(db, shipment):
    """Shape of a shipment in API responses."""
    carrier = await repo.carrier(db, shipment["carrier_id"])
    return {
        "id": shipment["id"],
        "status": shipment["status"],
        "carrier": carrier["name"],
        "tracking_url": carrier["tracking_url_template"].format(shipment["tracking_number"]),
    }
