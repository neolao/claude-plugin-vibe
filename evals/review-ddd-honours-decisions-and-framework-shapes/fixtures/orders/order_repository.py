import sqlite3

from orders.money import Money
from orders.order import Order
from orders.persistence import OrderLineRow, OrderRow


class OrderNotFound(Exception):
    pass


class OrderRepository:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get(self, order_id: str) -> Order:
        row = self._conn.execute("SELECT id, customer_id, status FROM orders WHERE id = ?", (order_id,)).fetchone()
        if row is None:
            raise OrderNotFound(order_id)
        return self._to_order(OrderRow(*row))

    def find_for_customer(self, customer_id: str) -> list[Order]:
        rows = self._conn.execute(
            "SELECT id, customer_id, status FROM orders WHERE customer_id = ?", (customer_id,)
        ).fetchall()
        return [self._to_order(OrderRow(*row)) for row in rows]

    def save(self, order: Order) -> None:
        head = OrderRow(order.order_id, order.customer_id, order.status)
        lines = [OrderLineRow(order.order_id, l.sku, l.qty, l.unit_price.cents) for l in order.lines]
        self._conn.execute(
            "INSERT OR REPLACE INTO orders (id, customer_id, status) VALUES (?, ?, ?)",
            (head.id, head.customer_id, head.status),
        )
        self._conn.execute("DELETE FROM order_lines WHERE order_id = ?", (order.order_id,))
        self._conn.executemany(
            "INSERT INTO order_lines (order_id, sku, qty, unit_cents) VALUES (?, ?, ?, ?)",
            [(l.order_id, l.sku, l.qty, l.unit_cents) for l in lines],
        )
        self._conn.commit()

    def _to_order(self, head: OrderRow) -> Order:
        order = Order(head.id, head.customer_id, head.status)
        rows = self._conn.execute(
            "SELECT order_id, sku, qty, unit_cents FROM order_lines WHERE order_id = ?", (head.id,)
        ).fetchall()
        for line in (OrderLineRow(*row) for row in rows):
            order.add_line(line.sku, line.qty, Money(line.unit_cents, "EUR"))
        return order
