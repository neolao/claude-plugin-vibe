---
type: llm
focus: last_message
criteria: |
  `test_reserve_deducts_from_stock` asserts the literal `7`, worked out by
  hand from the fixture's starting stock — not re-derived with the
  subtraction the implementation performs.

  PASS if no `high` or `medium` severity Tautological finding targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a hand-computed literal expectation tautological.
