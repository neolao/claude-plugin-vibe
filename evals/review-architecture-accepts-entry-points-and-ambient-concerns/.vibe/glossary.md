# Ubiquitous Language

## Order total
The price-times-quantity amount, discounted when the order carries a
promo, computed once for an order. Owned by `core/pricing.py`; every other
module reads the result, it never recomputes it.
_Sources: `core/pricing.py`_
