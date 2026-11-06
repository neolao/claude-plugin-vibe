"""Postgres access for orders."""

import psycopg2

from repositories.config import DSN


class OrderRepository:
    def save(self, order_id: str, total_cents: int) -> None:
        with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO orders (id, total_cents, placed_on) VALUES (%s, %s, CURRENT_DATE)",
                (order_id, total_cents),
            )

    def totals_since(self, day: str) -> list[int]:
        with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
            cur.execute("SELECT total_cents FROM orders WHERE placed_on >= %s", (day,))
            return [int(row[0]) for row in cur.fetchall()]
