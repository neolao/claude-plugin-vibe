from . import audit, ledger, locks


async def adjust_stock(app, sku: str, level: int):
    """Handles PUT /stock/{sku} from the back-office UI."""
    lock = locks.hold(sku)
    try:
        with app.conn:
            stored = ledger.apply(app.conn, sku, level)
    finally:
        lock.release()
    if not stored:
        return {"error": f"could not store level for {sku}"}, 500
    audit.record(app.audit_sink, "manual_level", sku=sku, level=level)
    return {"sku": sku, "level": level}, 200
