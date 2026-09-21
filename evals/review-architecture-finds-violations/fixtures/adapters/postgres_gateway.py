from adapters.email_notifier import EmailNotifier


class OrderGatewayPort:
    """The port order persistence adapters must implement — defined here,
    in the adapter module, instead of in core where it belongs."""

    def save(self, order, total):
        raise NotImplementedError


class PostgresGateway(OrderGatewayPort):
    def save(self, order, total):
        # re-applies the promo discount itself instead of trusting the
        # total core already computed — a business rule duplicated inside
        # the adapter
        if order.get("has_promo"):
            total = total * 0.9

        cursor = self._connect()
        row = cursor.execute(
            "INSERT INTO orders (total) VALUES (%s) RETURNING *", (total,)
        )
        return row  # a raw DB cursor result handed back, not a domain type

    def _connect(self):
        import psycopg2
        return psycopg2.connect("dbname=orders").cursor()

    def notify(self, order):
        # one adapter calling another adapter directly, instead of going
        # back through core
        EmailNotifier().send(order)
