"""Driven adapter: stores orders in Postgres behind core's OrderGatewayPort."""

import psycopg2

from adapters.config import DSN
from core.ports import OrderGatewayPort, OrderPersistenceError


class PostgresGateway(OrderGatewayPort):
    def save(self, order_id: str, total_cents: int) -> None:
        try:
            with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO orders (id, total_cents, placed_on) VALUES (%s, %s, CURRENT_DATE)",
                    (order_id, total_cents),
                )
        except psycopg2.Error as exc:
            raise OrderPersistenceError(str(exc)) from exc

    def totals_since(self, day: str) -> list[int]:
        try:
            with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
                cur.execute("SELECT total_cents FROM orders WHERE placed_on >= %s", (day,))
                return [int(row[0]) for row in cur.fetchall()]
        except psycopg2.Error as exc:
            raise OrderPersistenceError(str(exc)) from exc
