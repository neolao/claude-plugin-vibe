class BillingError(Exception):
    """Shown to the support agent in the console."""


def billing_error(result):
    return BillingError("refund failed")
