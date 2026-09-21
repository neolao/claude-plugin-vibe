def is_active(order):
    if order.get("archived"):
        return False
    return order["status"] in ("new", "processing", "shipped")


def get_or_create_cart(carts, user_id):
    cart = carts.get(user_id)
    if cart is None:
        cart = {"user_id": user_id, "items": []}
        carts[user_id] = cart
    return cart


def merge_adjacent_discounts(items):
    merged = []
    running_total = 0
    for item in items:
        if item["type"] == "discount":
            running_total += item["amount"]
            continue
        if running_total:
            merged.append({"type": "discount", "amount": running_total})
            running_total = 0
        merged.append(item)
    if running_total:
        merged.append({"type": "discount", "amount": running_total})
    return merged


def send_notification(message, channel):
    if channel == "email":
        print(f"Emailing: {message}")
    elif channel == "sms":
        print(f"Texting: {message}")
    else:
        print(f"Notifying via {channel}: {message}")


def notify_customer(order_id):
    send_notification(f"Order {order_id} placed", channel="email")


def notify_support(order_id):
    send_notification(f"Escalation for {order_id}", channel="sms")


def notify_webhook(order_id, endpoint):
    send_notification(f"Order {order_id} update", channel=endpoint)
