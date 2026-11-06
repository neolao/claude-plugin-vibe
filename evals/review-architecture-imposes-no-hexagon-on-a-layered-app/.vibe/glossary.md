# Ubiquitous Language

## Order total
What the customer pays for an order: the line amounts priced by the customer's
tier, with VAT applied once at the end. Computed once by the pricing policy
`OrderService` applies; the repository stores the result.
_Sources: `services/pricing.py`_

## Customer tier
`standard` or `wholesale`; wholesale customers get a volume rebate.
_Sources: `services/pricing.py`_
