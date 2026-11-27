import asyncio
import json

from shipping import labels, presenters, repo, tracking, zones

WAREHOUSES = [
    {"code": "LHR", "postcode": "TW6 2GA"},
    {"code": "MAN", "postcode": "M90 1QX"},
    {"code": "GLA", "postcode": "PA3 2SW"},
]


async def on_startup(app):
    """Runs once when the server starts, before it accepts requests."""
    app["warehouse_zones"] = {w["code"]: zones.zone_for(w["postcode"]) for w in WAREHOUSES}


async def list_shipments(request, db):
    """GET /customers/<customer_id>/shipments"""
    rows = await repo.shipments_with_carrier_for_customer(db, request.match_info["customer_id"])
    return [presenters.describe_row(row) for row in rows]


async def shipment_detail(request, db):
    """GET /shipments/<shipment_id>"""
    shipment = await repo.shipment(db, request.match_info["shipment_id"])
    return await presenters.describe(db, shipment)


async def print_label(request, db):
    """GET /shipments/<shipment_id>/label.pdf"""
    shipment = await repo.shipment(db, request.match_info["shipment_id"])
    return await asyncio.to_thread(labels.render_pdf, shipment)


async def carrier_webhook(request):
    """POST /webhooks/carrier — carriers push one scan event per parcel movement."""
    event = json.loads(await request.text())
    tracking.record_scan(event["tracking_number"], event["status"], event["scanned_at"])
    return {"ok": True}


async def tracking_status(request):
    """GET /track/<tracking_number>"""
    return {"status": tracking.latest_status(request.match_info["tracking_number"])}
