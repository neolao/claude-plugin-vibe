"""Order records."""

import sqlite3

DB_PATH = "/var/data/portal.db"


def render(owner_id, order_id):
    """The detail page of one of the owner's orders."""
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute(
        "SELECT total_cents, address FROM orders WHERE id = ? AND owner_id = ?",
        (order_id, owner_id),
    ).fetchone()
    if row is None:
        return "not found", 404
    return f"<html><body>{row[0]} cents to {row[1]}</body></html>"
