---
type: llm
focus: last_message
criteria: |
  The backlog item's criterion 1 says "older than 12 months"; the framing's
  decision "**Age limit** (🔒 MUST): 24 months, not 12" was settled later
  with the item in view and is the requirement. fixtures/archive.py keeps
  24 months (`MONTHS_KEPT = 24`), as decided.

  PASS if no `(gap)`, `(constraint)` or `(ambiguity)` finding is about the
  age limit (12 versus 24 months, criterion 1, `MONTHS_KEPT`).
  FAIL if any finding reports the 24-month limit as a gap on criterion 1,
  as a breach, or as an ambiguity between the item and the decision.
weight: 1
---

A decision that contradicts a criterion is the requirement; the
criterion it contradicts is neither a gap nor an ambiguity.
