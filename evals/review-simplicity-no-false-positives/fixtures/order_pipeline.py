def validate_order(order):
    if not order.get("items"):
        return False
    if order.get("total", 0) <= 0:
        return False
    return True


def calculate_shipping(order, region):
    if region == "domestic":
        return 5.0
    if region == "international":
        return 25.0
    return 15.0


def summarize_order(order):
    subtotal = sum(item["price"] for item in order["items"])
    shipping = calculate_shipping(order, order.get("region", "domestic"))
    tax = subtotal * 0.2
    total = subtotal + shipping + tax
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "tax": tax,
        "total": total,
    }
