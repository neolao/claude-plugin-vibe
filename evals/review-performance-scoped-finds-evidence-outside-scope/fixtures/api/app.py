import json

from shipping import labels, presenters, repo, tracking, zones


async def list_shipments(request, db):
    """GET /customers/<customer_id>/shipments"""
    shipments = await repo.shipments_for_customer(db, request.match_info["customer_id"])
    return [await presenters.describe(db, shipment) for shipment in shipments]


async def bulk_quote(request):
    """POST /quotes/bulk — a marketplace seller sends up to 5 000 parcels per call."""
    parcels = json.loads(await request.text())
    return [
        {"parcel_id": p["id"], "price_cents": zones.price_cents(p["postcode"], p["weight_g"])}
        for p in parcels
    ]


async def print_label(request, db):
    """GET /shipments/<shipment_id>/label.pdf"""
    shipment = await repo.shipment(db, request.match_info["shipment_id"])
    return labels.render_pdf(shipment)


async def carrier_webhook(request):
    """POST /webhooks/carrier — carriers push one scan event per parcel movement."""
    event = json.loads(await request.text())
    tracking.record_scan(event["tracking_number"], event["status"], event["scanned_at"])
    return {"ok": True}


async def tracking_status(request):
    """GET /track/<tracking_number>"""
    return {"status": tracking.latest_status(request.match_info["tracking_number"])}
