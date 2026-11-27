"""Order records."""

import sqlite3

DB_PATH = "/var/data/portal.db"


def render(order_id):
    """The detail page of one order."""
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT owner_id, total_cents, address FROM orders WHERE id = ?",
        (order_id,),
    ).fetchone()
    if row is None:
        return "not found", 404
    return f"<html><body>{row[1]} cents to {row[2]}</body></html>"
