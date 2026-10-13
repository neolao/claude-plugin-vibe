import psycopg2

from core.ports import OrderGatewayPort


class PostgresGateway(OrderGatewayPort):
    """Postgres implementation of the order gateway port."""

    def __init__(self, dsn):
        self._dsn = dsn

    def save(self, order_id, total_cents):
        with psycopg2.connect(self._dsn) as conn, conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO orders (id, total_cents) VALUES (%s, %s)",
                (order_id, total_cents),
            )
        return None
