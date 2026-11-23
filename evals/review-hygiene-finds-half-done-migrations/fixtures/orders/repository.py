import sqlite3

from orders.model import Order


class SqlOrderRepository:
    def __init__(self, url):
        self._db = sqlite3.connect(url, check_same_thread=False)

    def save(self, order):
        self._db.execute(
            "INSERT INTO orders (id, customer_id, total_cents, weight_grams, country, shipping_cents)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (order.id, order.customer_id, order.total_cents, order.weight_grams,
             order.country, order.shipping_cents),
        )
        self._db.commit()

    def get(self, order_id):
        row = self._db.execute(
            "SELECT id, customer_id, total_cents, weight_grams, country, shipping_cents"
            " FROM orders WHERE id = ?",
            (order_id,),
        ).fetchone()
        return Order(*row)
