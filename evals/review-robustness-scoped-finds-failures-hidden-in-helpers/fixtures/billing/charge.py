from db.tx import transaction


def charge_order(conn, gateway, order):
    """Called by the checkout flow once the customer confirms the payment."""
    with transaction(conn):
        conn.execute(
            "UPDATE orders SET status = 'charged' WHERE id = ?", (order["id"],)
        )
        gateway.capture(order["payment_id"], order["total_cents"])
    return {"id": order["id"], "charged": True}
