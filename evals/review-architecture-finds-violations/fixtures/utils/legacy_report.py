"""Weekly CSV export for finance. Nothing in core/ or adapters/ imports this
module, and it is not invoked by any entry point."""


def export_weekly_csv(orders):
    lines = ["order_id,total"]
    for order in orders:
        # reimplements the "order total" calculation instead of reusing
        # core.pricing.calculate_total — the same concept computed twice
        total = order["price"] * order["quantity"]
        if order.get("has_promo"):
            total *= 0.9
        lines.append(f"{order['id']},{total}")
    return "\n".join(lines)
