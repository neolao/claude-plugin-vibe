---
type: llm
focus: last_message
criteria: |
  `httpx` and `tabulate` are declared in `[project] dependencies` of
  fixtures/pyproject.toml. Nothing inside the scope (fixtures/orders/)
  imports them, but runtime code outside it does: fixtures/payments/gateway.py
  imports `httpx`, fixtures/cli/main.py imports `tabulate`.

  PASS if no `high` or `medium` severity `Unused` or `Misplaced` finding
  targets `httpx` or `tabulate`. A report whose only finding says the audit
  tool could not run passes.
  FAIL if either is flagged as unused or misplaced at high or medium
  severity.
weight: 1
---

Does not call a runtime dependency unused when its only importer sits
outside the path under review.
