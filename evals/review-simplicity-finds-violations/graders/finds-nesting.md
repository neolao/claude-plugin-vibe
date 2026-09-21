---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Nesting` (or clearly equivalent
  category name) finding on `validate_order` in
  fixtures/report_generator.py, for nesting an `if` inside a `for` inside
  nested `if`s to a depth clearly beyond 3 levels.
  FAIL if no finding flags `validate_order`'s nesting depth.
weight: 1
---

Reports `validate_order`'s deep if/for/if/if nesting as a `Nesting` finding.
