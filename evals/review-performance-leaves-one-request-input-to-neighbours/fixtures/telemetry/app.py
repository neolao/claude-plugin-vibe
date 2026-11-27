from telemetry import ingest


async def upload_trace(request):
    """POST /traces — a sensor uploads its diagnostic trace when asked."""
    chunks = []
    async for chunk in request.content.iter_chunked(64 * 1024):
        chunks.append(chunk)
    return {"stored": await ingest.store_trace(b"".join(chunks))}


async def list_events(request, db):
    """GET /devices/<device_id>/events?limit=N — the dashboard asks for 50 at a time."""
    limit = int(request.query.get("limit", 50))
    return await db.fetch(
        "SELECT * FROM events WHERE device_id = $1 ORDER BY at DESC LIMIT $2",
        request.match_info["device_id"],
        limit,
    )
