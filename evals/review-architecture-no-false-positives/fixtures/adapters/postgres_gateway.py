from core.ports import OrderGatewayPort
from adapters.config import DB_DSN


class PostgresGateway(OrderGatewayPort):
    """Postgres implementation of the order gateway port."""

    def save(self, order_id, total_cents):
        cursor = self._connect()
        cursor.execute(
            "INSERT INTO orders (id, total_cents) VALUES (%s, %s)",
            (order_id, total_cents),
        )
        return None

    def _connect(self):
        import psycopg2
        return psycopg2.connect(DB_DSN).cursor()
