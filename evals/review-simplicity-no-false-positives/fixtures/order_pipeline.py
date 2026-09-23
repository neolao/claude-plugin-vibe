def validate_order(order):
    if not order.get("items"):
        raise ValueError("order has no items")
    if order.get("total", 0) <= 0:
        raise ValueError("order total must be positive")


def calculate_shipping(subtotal, region):
    if region == "international":
        return 25.0
    if subtotal >= 50:
        return 0.0
    return 5.0


def summarize_order(order):
    subtotal = sum(item["price"] for item in order["items"])
    shipping = calculate_shipping(subtotal, order.get("region", "domestic"))
    tax = subtotal * 0.2
    total = subtotal + shipping + tax
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "tax": tax,
        "total": total,
    }
