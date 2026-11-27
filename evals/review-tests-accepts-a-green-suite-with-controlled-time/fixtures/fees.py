"""Transfer fees. The rule is stated in README.md."""

FEE_CAP = 5.0


def transfer_fee(amount):
    """Fee charged on an outgoing transfer of `amount`."""
    return min(round(amount * 0.02, 2), FEE_CAP)
