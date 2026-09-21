"""Weekly CSV export produced for the finance team."""


def export_weekly_csv(orders):
    lines = ["order_id,total"]
    for order in orders:
        total = order["price"] * order["quantity"]
        if order.get("has_promo"):
            total *= 0.9
        lines.append(f"{order['id']},{total}")
    return "\n".join(lines)
