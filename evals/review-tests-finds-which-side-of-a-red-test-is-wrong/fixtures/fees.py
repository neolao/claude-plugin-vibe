"""Transfer fees. The rule is stated in README.md."""


def transfer_fee(amount):
    """Fee charged on an outgoing transfer of `amount`."""
    return round(amount * 0.02, 2)
