# Module: core

**Role:** Order placement and the pricing rules per customer tier, with the
interfaces the business logic needs from the outside under `core/ports/`.
**Files:** `core/order_service.py`, `core/ports/order_gateway.py`, `core/pricing/policy.py`
**Exports:** `OrderService.place(order_id, line_amounts_cents, customer_tier) -> int`, `OrderGatewayPort`, `PricingPolicy`, `StandardPricing`, `WholesalePricing`, `policy_for(customer_tier) -> PricingPolicy`
**Depends on:** (none)
