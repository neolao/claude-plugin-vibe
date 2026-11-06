import sqlite3

from orders.money import Money
from orders.order import Order

_COLUMNS = "id, customer_id, status"


class OrderNotFound(Exception):
    pass


class OrderRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self, order_id: str) -> Order:
        row = self._conn.execute(f"SELECT {_COLUMNS} FROM orders WHERE id = ?", (order_id,)).fetchone()
        if row is None:
            raise OrderNotFound(order_id)
        return self._to_order(row)

    def find_for_customer(self, customer_id: str) -> list[Order]:
        rows = self._conn.execute(f"SELECT {_COLUMNS} FROM orders WHERE customer_id = ?", (customer_id,)).fetchall()
        return [self._to_order(row) for row in rows]

    def save(self, order: Order) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO orders (id, customer_id, status) VALUES (?, ?, ?)",
            (order.order_id, order.customer_id, order.status),
        )
        self._conn.execute("DELETE FROM order_lines WHERE order_id = ?", (order.order_id,))
        self._conn.executemany(
            "INSERT INTO order_lines (order_id, sku, qty, unit_cents) VALUES (?, ?, ?, ?)",
            [(order.order_id, line.sku, line.qty, line.unit_price.cents) for line in order.lines],
        )
        self._conn.commit()

    def _to_order(self, row) -> Order:
        order = Order(row[0], row[1], row[2])
        lines = self._conn.execute(
            "SELECT sku, qty, unit_cents FROM order_lines WHERE order_id = ?", (row[0],)
        ).fetchall()
        for sku, qty, unit_cents in lines:
            order.add_line(sku, qty, Money(unit_cents, "EUR"))
        return order
