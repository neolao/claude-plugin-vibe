---
type: llm
focus: last_message
criteria: |
  `ACTIVE_PROMOTIONS` in fixtures/orders/promotions.py is filled by
  `configure_promotions`, whose only caller in the repository is
  `main()` in fixtures/main.py, once at startup; nothing else writes to the
  list.

  PASS if no `high` or `medium` severity Mutable global state finding
  targets `ACTIVE_PROMOTIONS` or `configure_promotions`. A report with no
  findings at all passes.
  FAIL if either is flagged at high or medium severity as mutable global
  state.
weight: 1
---

Does not call a module-level list configured once by the entry point mutable
global state. The single caller sits outside the path under review.
