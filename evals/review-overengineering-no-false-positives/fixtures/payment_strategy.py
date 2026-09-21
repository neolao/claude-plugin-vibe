class DiscountStrategy:
    def apply(self, subtotal):
        raise NotImplementedError


class PercentageDiscount(DiscountStrategy):
    def __init__(self, rate):
        self._rate = rate

    def apply(self, subtotal):
        return subtotal * (1 - self._rate)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self._amount = amount

    def apply(self, subtotal):
        return max(subtotal - self._amount, 0)


def price_order(order):
    # both strategies are actually selected at checkout, depending on which
    # promo type the customer applied
    strategy = (
        PercentageDiscount(order["promo_rate"])
        if order["promo_type"] == "percentage"
        else FixedAmountDiscount(order["promo_amount"])
    )
    return strategy.apply(order["subtotal"])


class HttpClientConfig:
    def __init__(self, timeout_seconds):
        self.timeout_seconds = timeout_seconds


def build_internal_client():
    # internal network calls fail fast
    return HttpClientConfig(timeout_seconds=2)


def build_external_client():
    # third-party payment gateway is slower and less reliable
    return HttpClientConfig(timeout_seconds=30)
