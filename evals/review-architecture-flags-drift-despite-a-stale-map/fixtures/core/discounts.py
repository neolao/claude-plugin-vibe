"""Promo codes: a percentage off the subtotal, capped per order. Rates are maintained by marketing."""

import psycopg2

from adapters.config import DSN

CAP_CENTS = 5_000


def discount_for(code: str | None, subtotal_cents: int) -> int:
    if code is None:
        return 0
    with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
        cur.execute("SELECT percent FROM promo_codes WHERE code = %s", (code,))
        row = cur.fetchone()
    if row is None:
        return 0
    return min(subtotal_cents * int(row[0]) // 100, CAP_CENTS)
