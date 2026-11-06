"""Wording of the customer-facing messages."""


def confirmation_subject(order_id: str) -> str:
    return f"Order {order_id} confirmed"


def confirmation_body(total_cents: int) -> str:
    return f"Total: {total_cents / 100:.2f}"
