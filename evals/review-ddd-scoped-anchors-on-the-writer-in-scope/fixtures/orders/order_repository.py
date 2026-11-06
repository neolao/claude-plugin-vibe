import sqlite3

from customers.address import Address
from orders.money import Money
from orders.order import Order

_COLUMNS = "id, buyer_id, street, city, postcode, status"


class OrderNotFound(Exception):
    pass


class OrderRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self, order_id: str) -> Order:
        row = self._conn.execute(
            f"SELECT {_COLUMNS} FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        if row is None:
            raise OrderNotFound(order_id)
        return self._to_order(row)

    def find_for_buyer(self, buyer_id: str) -> list[Order]:
        rows = self._conn.execute(
            f"SELECT {_COLUMNS} FROM orders WHERE buyer_id = ?", (buyer_id,)
        ).fetchall()
        return [self._to_order(row) for row in rows]

    def find_unpaid(self, days: int):
        return self._conn.execute(
            f"SELECT {_COLUMNS}, created_at FROM orders"
            " WHERE status = 'open' AND created_at < date('now', ?)",
            (f"-{days} days",),
        ).fetchall()

    def save(self, order: Order) -> None:
        address = order.shipping_address
        self._conn.execute(
            "INSERT OR REPLACE INTO orders (id, buyer_id, street, city, postcode, status)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (order.order_id, order.buyer_id, address.street, address.city, address.postcode, order.status),
        )
        self._conn.execute("DELETE FROM order_lines WHERE order_id = ?", (order.order_id,))
        self._conn.executemany(
            "INSERT INTO order_lines (order_id, sku, qty, unit_cents) VALUES (?, ?, ?, ?)",
            [(order.order_id, line.sku, line.qty, line.unit_price.cents) for line in order.lines],
        )
        self._conn.commit()

    def _to_order(self, row) -> Order:
        order = Order(row[0], row[1], Address(row[2], row[3], row[4]), row[5])
        lines = self._conn.execute(
            "SELECT sku, qty, unit_cents FROM order_lines WHERE order_id = ?", (row[0],)
        ).fetchall()
        for sku, qty, unit_cents in lines:
            order.add_line(sku, qty, Money(unit_cents, "EUR"))
        return order
