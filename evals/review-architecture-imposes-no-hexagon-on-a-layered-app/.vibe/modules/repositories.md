# Module: repositories

**Role:** Postgres access for orders: the one layer that opens connections and
runs SQL.
**Files:** `repositories/order_repository.py`, `repositories/config.py`
**Exports:** `OrderRepository.save(order_id, total_cents)`, `OrderRepository.totals_since(day) -> list[int]`
**Depends on:** (none)
