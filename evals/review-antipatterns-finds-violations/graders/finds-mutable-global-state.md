---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Mutable global state` (or
  clearly equivalent category name) finding on the module-level `_REGISTRY`
  dict in fixtures/config.py, mutated from both `register` and `unregister`.
  FAIL if no finding flags `_REGISTRY` for this reason.
weight: 1
---

Reports the module-level `_REGISTRY` dict in fixtures/config.py as a
Mutable global state finding.
