# Called from the checkout page to show the delivery price before payment.
from orders.money import Money
from orders.order import Order

GRAMS_PER_SKU = {"SOCK-01": 60, "MUG-02": 350}
PRICE_PER_KG = Money(450, "EUR")


def quote(order: Order) -> Money:
    grams = sum(GRAMS_PER_SKU.get(line.sku, 500) * line.qty for line in order.lines)
    kilos = max(1, -(-grams // 1000))
    return PRICE_PER_KG.times(kilos)
