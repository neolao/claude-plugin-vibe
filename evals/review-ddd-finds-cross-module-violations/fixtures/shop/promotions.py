# Called from the checkout flow when the customer enters a bundle code.
from dataclasses import dataclass

from cart import Cart, Line
from money import Money


@dataclass(frozen=True)
class Bundle:
    code: str
    sku: str
    qty: int


# Maintained by the marketing team.
BUNDLES = {
    "SUMMER": Bundle("SUMMER", "SOCK-01", 12),
    "DUO": Bundle("DUO", "MUG-02", 2),
}


def apply_bundle(cart: Cart, code: str) -> None:
    bundle = BUNDLES[code]
    cart._lines.append(Line(bundle.sku, bundle.qty, Money(0, "EUR")))
