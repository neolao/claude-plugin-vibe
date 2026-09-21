---
type: llm
focus: last_message
criteria: |
  Both `InventoryService` error paths — non-positive quantity and
  insufficient stock — have dedicated, active `assertRaises` tests.

  PASS if no `high` or `medium` severity Missing negative cases or Coverage
  gap finding claims an untested error path here.
  FAIL if one is reported.
weight: 1
---

Invents no missing negative case where both error paths are tested.
