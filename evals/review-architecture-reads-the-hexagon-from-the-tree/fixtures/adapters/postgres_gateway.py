"""Stores orders in Postgres."""

import psycopg2

from adapters.config import DSN
from core.ports.order_gateway import OrderGatewayPort, OrderPersistenceError


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
