def validate_order(order):
    if order:
        if "items" in order:
            for item in order["items"]:
                if item.get("price"):
                    if item["price"] > 0:
                        return True
    return False


def classify_order(order):
    status = order.get("status")
    total = order.get("total", 0)
    if status == "new":
        if total > 1000:
            return "new-high-value"
        elif total > 500:
            return "new-medium-value"
        else:
            return "new-low-value"
    elif status == "processing":
        if total > 1000:
            return "processing-high-value"
        elif total > 500:
            return "processing-medium-value"
        else:
            return "processing-low-value"
    elif status == "shipped":
        if total > 1000:
            return "shipped-high-value"
        else:
            return "shipped-low-value"
    elif status == "cancelled":
        return "cancelled"
    elif status == "returned":
        return "returned"
    elif status == "on_hold":
        return "on_hold"
    elif status == "refunded":
        if total > 1000:
            return "refunded-high-value"
        else:
            return "refunded-low-value"
    else:
        return "unknown"


def generate_report(order_history):
    lines = []
    lines.append("=== Order Report ===")
    lines.append("")
    lines.append("Order ID: " + str(order_history.get("id")))
    lines.append("Customer: " + str(order_history.get("customer")))
    lines.append("Date: " + str(order_history.get("date")))
    lines.append("Status: " + str(order_history.get("status")))
    lines.append("")
    lines.append("--- Items ---")
    for item in order_history.get("items", []):
        lines.append("  - " + str(item.get("name")) + ": " + str(item.get("price")))
    lines.append("")
    lines.append("--- Totals ---")
    subtotal = sum(i.get("price", 0) for i in order_history.get("items", []))
    lines.append("Subtotal: " + str(subtotal))
    tax = subtotal * 0.2
    lines.append("Tax: " + str(tax))
    shipping = order_history.get("shipping", 0)
    lines.append("Shipping: " + str(shipping))
    total = subtotal + tax + shipping
    lines.append("Total: " + str(total))
    lines.append("")
    lines.append("--- Payment ---")
    lines.append("Method: " + str(order_history.get("payment_method")))
    lines.append("Last 4: " + str(order_history.get("card_last4")))
    lines.append("")
    lines.append("--- Shipping Address ---")
    address = order_history.get("address", {})
    lines.append("Street: " + str(address.get("street")))
    lines.append("City: " + str(address.get("city")))
    lines.append("State: " + str(address.get("state")))
    lines.append("Zip: " + str(address.get("zip")))
    lines.append("Country: " + str(address.get("country")))
    lines.append("")
    lines.append("--- Notes ---")
    lines.append(str(order_history.get("notes", "None")))
    lines.append("")
    lines.append("--- Loyalty ---")
    lines.append("Points earned: " + str(order_history.get("points_earned", 0)))
    lines.append("Points balance: " + str(order_history.get("points_balance", 0)))
    lines.append("")
    lines.append("=== End of Report ===")
    return "\n".join(lines)
