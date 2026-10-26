"""Stock ledger. Every change of quantity goes through record_movement."""

from hooks import after_movement


def record_movement(product, delta, mailer, manager_email):
    product["quantity"] += delta
    after_movement(product, product["quantity"], mailer, manager_email)
    return product["quantity"]
