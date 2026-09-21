def checkout(order_id, db):
    """Request handler for POST /orders/<order_id>/checkout."""
    order_lines = db.get_order_lines(order_id)
    product_ids = [line["product_id"] for line in order_lines]
    products_by_id = db.get_products_by_ids(product_ids)

    total = 0
    for line in order_lines:
        product = products_by_id[line["product_id"]]
        total += product["price"] * line["quantity"]

    db.mark_paid(order_id, total)
    return {"order_id": order_id, "total": total}
