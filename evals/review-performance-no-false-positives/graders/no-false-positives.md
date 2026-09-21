---
type: llm
focus: last_message
criteria: |
  The fixtures each superficially resemble a performance defect but are
  already mitigated or out of scope for this dimension:
  - `checkout_handler.py`: the loop over `order_lines` looks like the classic
    N+1 shape, but the product lookup is a single batched
    `db.get_products_by_ids(...)` call before the loop; the loop itself only
    does in-memory arithmetic over data already fetched.
  - `catalog_cache.py`: `_price_cache` is fed by external `sku` values like an
    unbounded cache would be, but it is explicitly capped at
    `_MAX_CACHE_ENTRIES` with eviction when full.
  - `inventory_service.py`'s `has_conflicting_reservation` looks like it scans
    a collection, but `reservations_by_slot` is a dict keyed by
    `(warehouse, slot)`, so the lookup is O(1), not a linear search.
  - `inventory_service.py`'s `load_warehouse_config` looks like blocking I/O
    on a request path, but its docstring states it runs once at process
    startup, before the server accepts requests — not on the hot path.
  - `render_loop.py`'s `update_frame` looks like a per-frame allocation and
    per-object draw call loop, but it reuses the module-level
    `_transform_buffer` (cleared, not reallocated) and batches draw calls by
    texture via `batches_by_texture` instead of issuing one draw call per
    entity.
  - `migrate_price_history.py` has an O(n*m) nested loop, but its own
    docstring states it is a one-shot migration script run manually by an
    operator, not part of the running server — checklists for this dimension
    explicitly exclude one-shot migrations and scripts.

  PASS if the response reports no `high` or `medium` severity N+1,
  Complexity, Blocking, Unbounded, or Real-time finding on this code — either
  no findings at all, or only `low` severity style notes unrelated to these
  already-mitigated or out-of-scope patterns.
  FAIL if it flags the batched product fetch as N+1, the bounded cache as
  unbounded, the dict-keyed lookup as a linear scan, the startup-time config
  load as blocking a request, the buffer-reusing/batched render loop as
  allocating or unbatched, or the migration script's nested loop as a
  Complexity issue.
weight: 2
---

Does not invent performance findings on code that already mitigates each
pattern, or that is explicitly out of scope (a one-shot migration script).
