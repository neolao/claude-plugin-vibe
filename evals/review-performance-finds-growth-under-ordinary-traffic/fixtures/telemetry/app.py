import json

from telemetry import devices, ingest


async def heartbeat(request):
    """POST /heartbeat — every installed sensor posts one every 30 seconds."""
    event = json.loads(await request.text())
    devices.record_heartbeat(event["device_id"], event["seen_at"], event["firmware"])
    return {"ok": True}


async def upload_trace(request):
    """POST /traces — a sensor uploads its diagnostic trace when asked."""
    chunks = []
    async for chunk in request.content.iter_chunked(64 * 1024):
        chunks.append(chunk)
    return {"stored": await ingest.store_trace(b"".join(chunks))}


async def device_status(request):
    """GET /devices/<device_id>"""
    return devices.status(request.match_info["device_id"])
