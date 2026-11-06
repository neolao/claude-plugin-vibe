# Module: core

**Role:** Pure business/domain logic for order pricing, promo discounts and
placement. No I/O, no framework, database, or mail imports — it depends only
on ports it owns.
**Files:** `core/order_service.py`, `core/pricing.py`, `core/discounts.py`, `core/ports.py`
**Exports:** `OrderService.place(order_id, line_amounts_cents, promo_code) -> int`, `calculate_total(line_amounts_cents, discount_cents) -> int`, `discount_for(code, subtotal_cents) -> int`, `OrderGatewayPort`, `NotifierPort`
**Depends on:** (none — the innermost layer)
