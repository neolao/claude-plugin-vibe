---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Non-idiomatic` (or clearly
  equivalent category name) finding on `format_items` in
  fixtures/discount.py, for the manual loop-and-append that a list
  comprehension (`[item.upper() for item in items]`) would express more
  clearly.
  FAIL if no finding flags `format_items`'s loop as a non-idiomatic detour.
weight: 1
---

Reports `format_items`'s manual accumulation loop as a `Non-idiomatic`
finding.
