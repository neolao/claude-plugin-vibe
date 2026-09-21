from core.ports import OrderGatewayPort
from adapters.config import DB_DSN


class PostgresGateway(OrderGatewayPort):
    """Implements the port core owns. Talks to Postgres and to Postgres
    alone — no other adapter is ever called from here."""

    def save(self, order_id, total_cents):
        cursor = self._connect()
        cursor.execute(
            "INSERT INTO orders (id, total_cents) VALUES (%s, %s)",
            (order_id, total_cents),
        )
        # returns nothing — core only needs to know the write happened,
        # never a driver-specific cursor or row
        return None

    def _connect(self):
        import psycopg2
        return psycopg2.connect(DB_DSN).cursor()
