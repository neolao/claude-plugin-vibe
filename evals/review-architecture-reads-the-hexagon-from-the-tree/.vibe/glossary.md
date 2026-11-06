# Ubiquitous Language

## Order total
What the customer pays for an order: the line amounts priced by the customer's
tier, with VAT applied once at the end. Computed once by the pricing policy
`OrderService` applies; the gateway stores the result.
_Sources: `core/pricing/policy.py`_

## Customer tier
`standard` or `wholesale`; wholesale customers get a volume rebate.
_Sources: `core/pricing/policy.py`_
