---
type: llm
focus: last_message
criteria: |
  Each inventory test class builds a fresh `InventoryService` in `setUp`,
  and each pricing test builds its own mock and `PricingService` inline;
  there is no module-level mutable state, so no test depends on another or
  on ordering. A report with no Isolation finding at all passes.

  PASS if no `high` or `medium` severity Isolation finding is reported.
  FAIL if one is.
weight: 1
---

Does not call per-test construction order-dependent.
