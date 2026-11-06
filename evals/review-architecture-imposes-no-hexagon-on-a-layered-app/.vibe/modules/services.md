# Module: services

**Role:** Order placement and the pricing rules it applies; talks to the
database through the repositories layer only.
**Files:** `services/order_service.py`, `services/pricing.py`
**Exports:** `OrderService.place(order_id, line_amounts_cents, customer_tier) -> int`, `PricingPolicy`, `StandardPricing`, `WholesalePricing`
**Depends on:** [`modules/repositories.md`](repositories.md)
