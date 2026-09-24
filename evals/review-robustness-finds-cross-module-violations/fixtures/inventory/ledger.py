import logging
import sqlite3

log = logging.getLogger(__name__)


def apply(conn: sqlite3.Connection, sku: str, level: int) -> bool:
    try:
        conn.execute("UPDATE stock SET level = ? WHERE sku = ?", (level, sku))
        return True
    except sqlite3.Error:
        log.warning("could not store level %s for %s", level, sku)
        return False
