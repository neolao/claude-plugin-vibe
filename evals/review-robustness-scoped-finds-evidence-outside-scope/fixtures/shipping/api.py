from events import bus


async def hold_parcel(app, parcel_id: str, reason: str):
    """Handles PUT /parcels/{parcel_id}/hold from the back-office UI."""
    app.holds[parcel_id] = reason
    bus.publish(app.dashboard, "parcel.held", parcel_id=parcel_id, reason=reason)
    return {"id": parcel_id, "held": True}, 200
