# Module: core

**Role:** Pure business/domain logic for order pricing and placement. No I/O, no
framework, database, or mail imports — it depends only on the port it owns.
**Files:** `core/order_service.py`, `core/pricing.py`, `core/ports.py`
**Exports:** `OrderRecord`, `OrderService.place(order_id, line_amounts_cents) -> OrderRecord`, `calculate_total(line_amounts_cents) -> int`, `OrderGatewayPort`
**Depends on:** (none — the innermost layer)
