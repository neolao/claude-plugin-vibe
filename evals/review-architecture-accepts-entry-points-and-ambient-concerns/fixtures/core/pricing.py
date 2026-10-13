def calculate_total(order):
    total_cents = order["unit_price_cents"] * order["quantity"]
    if order.get("has_promo"):
        total_cents = total_cents * 9 // 10
    return total_cents
