from . import ledger, locks
from .errors import SupplierError, SyncFailed


def sync_skus(conn, client, skus):
    consumed = []
    for sku in skus:
        lock = locks.hold(sku)
        level = client.stock_level(sku)
        ledger.apply(conn, sku, level)
        lock.release()
        consumed.append(sku)
    return consumed


def run(conn, client, skus, cursor):
    """Called by worker.tick; the cursor tells the supplier which changes we consumed."""
    try:
        with conn:
            consumed = sync_skus(conn, client, skus)
    except SupplierError as exc:
        raise SyncFailed(exc)
    cursor.advance(consumed)
