---
type: llm
focus: last_message
criteria: |
  The classifier judges the findings it is given; it does not review the
  code for new ones.

  PASS if every entry under `## CLASSIFIED findings` and `## DISCARDED`
  traces back to finding 1 or finding 2 of the prompt (same line, same
  defect), and `## DISCARDED` does not list finding 1 as dropped.
  FAIL if a kept or discarded entry describes a defect neither raw finding
  mentioned (a naming remark, a missing test, a docstring, an unused
  import…), or if finding 1 is dropped.
weight: 2
---

No new findings appear out of nowhere, and no valid one is dropped.
