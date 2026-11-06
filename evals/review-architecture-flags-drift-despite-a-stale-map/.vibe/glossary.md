# Ubiquitous Language

## Order total
What the customer pays for an order: the line amounts minus the promo
discount, never below zero, with VAT applied once at the end. Computed once by
`calculate_total`; the gateway stores the result and the nightly job sums it.
_Sources: `core/pricing.py`_
