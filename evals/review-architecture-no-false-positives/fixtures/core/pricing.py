def calculate_total(order):
    total = order["price"] * order["quantity"]
    if order.get("has_promo"):
        total *= 0.9
    return total
