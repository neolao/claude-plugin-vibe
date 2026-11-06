class DiscountStrategy:
    def apply(self, subtotal_cents):
        raise NotImplementedError


class PercentageDiscount(DiscountStrategy):
    def __init__(self, rate):
        self._rate = rate

    def apply(self, subtotal_cents):
        return subtotal_cents - subtotal_cents * self._rate // 100


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount_cents):
        self._amount_cents = amount_cents

    def apply(self, subtotal_cents):
        return max(subtotal_cents - self._amount_cents, 0)


def price_order(order):
    """Called at checkout; the promo type comes from the code the customer entered."""
    if order["promo_type"] == "percentage":
        strategy = PercentageDiscount(order["promo_rate"])
    else:
        strategy = FixedAmountDiscount(order["promo_amount_cents"])
    return strategy.apply(order["subtotal_cents"])
