# Called from the checkout page to show the delivery price before payment.
from cart import Cart
from money import Money

GRAMS_PER_SKU = {"SOCK-01": 60, "MUG-02": 350}
PRICE_PER_KG = Money(450, "EUR")


def quote(cart: Cart) -> Money:
    grams = sum(GRAMS_PER_SKU.get(line.sku, 500) * line.qty for line in cart.lines)
    kilos = max(1, -(-grams // 1000))
    return PRICE_PER_KG.times(kilos)
