def checkout(order_id, db):
    """Request handler for POST /orders/<order_id>/checkout."""
    order_lines = db.get_order_lines(order_id)

    total = 0
    for line in order_lines:
        product = db.get_product(line["product_id"])
        total += product["price"] * line["quantity"]

    db.mark_paid(order_id, total)
    return {"order_id": order_id, "total": total}
