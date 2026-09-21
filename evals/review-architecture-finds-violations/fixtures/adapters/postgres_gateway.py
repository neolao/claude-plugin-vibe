from adapters.email_notifier import EmailNotifier


class OrderGatewayPort:
    """The interface order persistence adapters implement."""

    def save(self, order, total):
        raise NotImplementedError


class PostgresGateway(OrderGatewayPort):
    def save(self, order, total):
        if order.get("has_promo"):
            total = total * 0.9

        cursor = self._connect()
        row = cursor.execute(
            "INSERT INTO orders (total) VALUES (%s) RETURNING *", (total,)
        )
        return row

    def _connect(self):
        import psycopg2
        return psycopg2.connect("dbname=orders").cursor()

    def notify(self, order):
        EmailNotifier().send(order)
