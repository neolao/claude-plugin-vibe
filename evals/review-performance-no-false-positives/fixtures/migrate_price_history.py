"""One-shot migration script: run once by an operator to backfill
`order_count` on historical products. Not part of the running server and
not on any request path."""


def backfill_order_counts(all_products, all_orders):
    for product in all_products:
        product["order_count"] = 0
        for order in all_orders:
            if order.get("product_id") == product["id"]:
                product["order_count"] += 1
    return all_products
