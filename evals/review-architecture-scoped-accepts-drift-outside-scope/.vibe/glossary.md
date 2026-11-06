# Ubiquitous Language

## Order total
What the customer pays for an order: the line amounts minus the promo
discount, never below zero, with VAT applied once at the end. Computed once by
`calculate_total`; the gateway stores the result.
_Sources: `core/pricing.py`_

## Promo discount
The amount a promo code takes off the subtotal: a percentage per code, capped
per order. Computed by `discount_for`.
_Sources: `core/discounts.py`_
