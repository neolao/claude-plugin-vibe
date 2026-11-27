from orders.repository import OrderRepository


class SqlOrderRepository(OrderRepository):
    def __init__(self, db):
        self._db = db

    def shipped_on(self, day):
        rows = self._db.fetch_all(
            "SELECT id, customer_email, invoice_json FROM orders WHERE shipped_on = %s",
            (day,),
        )
        return [
            {"id": row[0], "customer": {"email": row[1]}, "invoice": row[2]}
            for row in rows
        ]
