# Module: core

**Role:** Pure business/domain logic for order pricing and placement, plus the
domain events placement raises. No I/O, no framework, database, or mail
imports — it depends only on ports it owns.
**Files:** `core/order_service.py`, `core/pricing.py`, `core/ports.py`, `core/events.py`
**Exports:** `OrderService.place(order_id, line_amounts_cents) -> int`, `calculate_total(line_amounts_cents) -> int`, `OrderPlaced`, `OrderGatewayPort`, `NotifierPort`
**Depends on:** (none — the innermost layer)
