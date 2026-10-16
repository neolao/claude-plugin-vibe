---
type: llm
focus: last_message
criteria: |
  `httpx` is declared in the `dev` extra of fixtures/pyproject.toml, but
  fixtures/payments/gateway.py — runtime code outside the scope — imports
  it to call the payment provider.
  PASS if the reported findings include a `Misplaced` finding on `httpx`
  that names fixtures/payments/gateway.py (or the `payments` package) as
  the runtime importer and suggests moving it to `[project] dependencies`.
  FAIL if `httpx` is not flagged, is flagged as `Unused` (never imported)
  instead of `Misplaced`, or the finding names no importer outside the
  scope.
weight: 1
---

Reports `httpx`, a dev-extra package that runtime code imports, as a
Misplaced finding. Nothing inside fixtures/orders/ imports it: an agent
that greps only the scope calls it unused.
