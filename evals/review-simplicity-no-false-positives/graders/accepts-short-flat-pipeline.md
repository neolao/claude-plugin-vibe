---
type: llm
focus: last_message
criteria: |
  `validate_order`, `calculate_shipping`, and `summarize_order` in
  fixtures/order_pipeline.py are each under fifteen lines, at most one level
  of nesting, and well under ten branches.

  PASS if no `high` or `medium` severity Complexity, Length, or Nesting
  finding targets any of the three.
  FAIL if any of them is flagged as a complexity, length, or nesting hotspot
  at high or medium severity.
weight: 1
---

Does not call short, flat, low-branching functions complexity hotspots.
