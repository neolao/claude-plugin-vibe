"""Customer e-mails sent by the checkout and the back office."""

SUBJECT_PREFIX = "[Shop] "


def order_confirmed(order):
    return {
        "subject": f"{SUBJECT_PREFIX}Order {order.reference} confirmed",
        "body": f"Thank you, your order {order.reference} is being prepared.",
    }


def order_shipped(order):
    return {
        "subject": f"{SUBJECT_PREFIX}Order {order.reference} shipped",
        "body": f"Your order {order.reference} left our warehouse today.",
    }
