---
type: llm
focus: last_message
criteria: |
  `.vibe/decisions/001-import-time-handler-registry.md` mandated the
  module-level `HANDLERS` dict, but its status is `superseded by 002`, and
  `002-handlers-injected-into-dispatcher.md` (accepted) retires the
  registry. The dict is still written from fixtures/shop/handlers/billing.py
  and fixtures/shop/handlers/shipping.py (`register` at import) and from
  fixtures/shop/admin.py (`pop`, `register`).

  PASS if the reported findings include a `Mutable global state` (or
  clearly equivalent category name) finding on `HANDLERS` in
  fixtures/shop/handlers/__init__.py (or on `register`) whose ISSUE or
  SUGGESTION names at least one of the writers: billing.py, shipping.py or
  admin.py.
  FAIL if no finding flags `HANDLERS` as mutable global state, or if the
  only reason given for silence is decision 001.
weight: 2
---

Reports the registry as Mutable global state: a superseded decision
mandates nothing, and the accepted one retires the shape.
