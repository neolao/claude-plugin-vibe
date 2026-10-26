"""Stock movement hooks. Registered once at application start."""

from notify import warn_if_low


def after_movement(product, new_quantity, mailer, manager_email):
    return warn_if_low(product, new_quantity, mailer, manager_email)
