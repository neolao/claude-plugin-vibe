from common.errors import billing_error


def refund_order(gateway, order):
    """Handles POST /orders/{id}/refund from the support console."""
    result = gateway.refund(order["payment_id"], order["total_cents"])
    if not result.ok:
        raise billing_error(result)
    return {"id": order["id"], "refunded": True}
