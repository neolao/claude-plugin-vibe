---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Redundant logic` (or clearly
  equivalent category name) finding on `is_expired` in fixtures/discount.py,
  for the `if flag: return True else: return False` pattern that could be a
  bare `return flag`/`return bool(flag)`.
  FAIL if no finding flags `is_expired`'s redundant if/else.
weight: 1
---

Reports `is_expired`'s if/else returning literal `True`/`False` as a
`Redundant logic` finding.
