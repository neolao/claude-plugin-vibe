import psycopg2

from core.ports import OrderGatewayPort, OrderPersistenceError
from adapters.config import DB_DSN


class PostgresGateway(OrderGatewayPort):
    """Postgres implementation of the order gateway port."""

    def save(self, order_id, total_cents):
        try:
            with psycopg2.connect(DB_DSN) as conn, conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO orders (id, total_cents) VALUES (%s, %s)",
                    (order_id, total_cents),
                )
        except psycopg2.Error as error:
            raise OrderPersistenceError(f"could not save order {order_id}") from error
        return None
