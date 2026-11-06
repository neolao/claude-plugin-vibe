"""Driven adapter: stores orders in Postgres behind core's OrderGatewayPort."""

import psycopg2

from adapters.config import DSN
from core.order_service import OrderRecord
from core.ports import OrderGatewayPort, OrderPersistenceError


class PostgresGateway(OrderGatewayPort):
    def save(self, order_id: str, total_cents: int) -> None:
        try:
            with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO orders (id, total_cents) VALUES (%s, %s)",
                    (order_id, total_cents),
                )
        except psycopg2.Error as exc:
            raise OrderPersistenceError(str(exc)) from exc

    def last_saved(self, order_id: str) -> OrderRecord:
        with psycopg2.connect(DSN) as conn, conn.cursor() as cur:
            cur.execute("SELECT total_cents FROM orders WHERE id = %s", (order_id,))
            row = cur.fetchone()
        return OrderRecord(order_id, int(row[0]))
