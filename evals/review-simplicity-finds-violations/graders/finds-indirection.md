---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Indirection` (or clearly
  equivalent category name) finding on `get_total` in fixtures/discount.py,
  for wrapping `calculate_total` with a call that adds no naming, default, or
  adaptation of its own.
  FAIL if no finding flags `get_total` as a pointless wrapper.
weight: 1
---

Reports `get_total`'s pure delegation to `calculate_total` as an
`Indirection` finding.
