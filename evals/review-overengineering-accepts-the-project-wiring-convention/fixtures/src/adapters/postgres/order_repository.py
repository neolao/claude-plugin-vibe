import json

from core.ports.order_repository import OrderRepository


class PostgresOrderRepository(OrderRepository):
    def __init__(self, db):
        self._db = db

    def add(self, order):
        self._db.execute(
            "INSERT INTO orders (id, status, lines_json) VALUES (%s, %s, %s)",
            (order["id"], order["status"], json.dumps(order["lines"])),
        )
