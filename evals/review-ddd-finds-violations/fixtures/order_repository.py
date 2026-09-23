def _fake_db():
    class _Db:
        def execute(self, *args, **kwargs):
            return self

        def fetchone(self):
            return {"id": "o1", "customer_id": "c1", "status": "open"}

    return _Db()


class OrderRepository:
    """Loads and stores orders."""

    def __init__(self):
        self._db = _fake_db()

    def find_by_id(self, order_id):
        row = self._db.execute(
            "SELECT * FROM orders WHERE id = %s", (order_id,)
        ).fetchone()
        return dict(row)

    def find_for_customer(self, customer_id):
        return self._db.execute(
            "SELECT * FROM orders WHERE customer_id = %s", (customer_id,)
        ).fetchone()

    def save(self, order_dict):
        self._db.execute(
            "UPDATE orders SET status = %s WHERE id = %s",
            (order_dict["status"], order_dict["order_id"]),
        )
