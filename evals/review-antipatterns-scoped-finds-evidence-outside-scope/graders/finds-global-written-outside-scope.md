---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Mutable global state` (or
  clearly equivalent category name) finding on the module-level
  `ACTIVE_PROMOTIONS` list in fixtures/orders/promotions.py whose ISSUE or
  SUGGESTION names at least one of the modules that write to it from
  outside the scope: fixtures/campaigns/admin.py (`append`/`remove`) or
  fixtures/campaigns/scheduler.py (`clear`/`extend`).
  FAIL if no finding flags `ACTIVE_PROMOTIONS` as mutable global state, or
  if the finding never mentions a writer in fixtures/campaigns/.
weight: 1
---

Reports `ACTIVE_PROMOTIONS` in fixtures/orders/promotions.py as Mutable
global state, naming a writer in fixtures/campaigns/. Inside the scope the
list is created empty and only read: the writers are only visible to an agent
that greps the whole repository.
