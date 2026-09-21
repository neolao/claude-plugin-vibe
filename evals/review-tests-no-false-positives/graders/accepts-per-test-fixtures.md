---
type: llm
focus: last_message
criteria: |
  Every test class builds a fresh `InventoryService` in `setUp`; there is no
  module-level mutable state, so no test depends on another or on ordering.

  PASS if no `high` or `medium` severity Isolation finding is reported.
  FAIL if one is.
weight: 1
---

Does not call per-test construction order-dependent.
