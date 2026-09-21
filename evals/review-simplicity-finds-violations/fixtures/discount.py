def is_expired(flag):
    if flag:
        return True
    else:
        return False


def calculate_total(order):
    return order["price"] * order["quantity"]


def get_total(order):
    return calculate_total(order)


def format_items(items):
    result = []
    for item in items:
        result.append(item.upper())
    return result


def send_notification(message, channel="email"):
    if channel == "email":
        print(f"Emailing: {message}")
    elif channel == "sms":
        print(f"Texting: {message}")
    else:
        print(f"Notifying via {channel}: {message}")


def notify_order_placed(order_id):
    send_notification(f"Order {order_id} placed", channel="email")


def notify_order_shipped(order_id):
    send_notification(f"Order {order_id} shipped", channel="email")


def notify_order_cancelled(order_id):
    send_notification(f"Order {order_id} cancelled", channel="email")
