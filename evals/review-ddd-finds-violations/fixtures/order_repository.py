def _fake_db():
    class _Db:
        def execute(self, *args, **kwargs):
            return self

        def fetchone(self):
            return {"id": "o1", "status": "open"}

    return _Db()


class OrderRepository:
    """Reads and writes orders directly against the orders table."""

    def __init__(self):
        self._db = _fake_db()

    def find_by_id(self, order_id):
        row = self._db.execute(
            f"SELECT * FROM orders WHERE id = '{order_id}'"
        ).fetchone()
        return dict(row)

    def save(self, order_dict):
        self._db.execute(
            "UPDATE orders SET status = ? WHERE id = ?",
            (order_dict["status"], order_dict["order_id"]),
        )
