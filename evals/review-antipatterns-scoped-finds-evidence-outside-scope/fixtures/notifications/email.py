"""Order confirmation email."""


def confirmation_body(order, total_cents):
    return f"Thanks for your order {order.id}. Total: {total_cents / 100:.2f} EUR"
