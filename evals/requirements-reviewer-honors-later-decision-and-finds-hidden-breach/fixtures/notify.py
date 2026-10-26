"""Low-stock warning. Called by hooks.after_movement."""

from tenacity import retry, stop_after_attempt


def build_message(product, quantity):
    return f"Low stock: {product['name']}"


@retry(stop=stop_after_attempt(3))
def send_email(mailer, to, body):
    mailer.send(to=to, subject="Low stock", body=body)


def warn_if_low(product, quantity, mailer, manager_email):
    if quantity < product["threshold"]:
        send_email(mailer, manager_email, build_message(product, quantity))
        return True
    return False
