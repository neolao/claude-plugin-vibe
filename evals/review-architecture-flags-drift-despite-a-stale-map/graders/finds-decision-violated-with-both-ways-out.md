---
type: llm
focus: last_message
criteria: |
  `.vibe/decisions/002-money-in-integer-cents.md` (status accepted) says
  every amount computation is integer arithmetic, never a float multiplied
  then rounded. `calculate_total` in fixtures/core/pricing.py computes
  `int(round(subtotal * (1 + VAT_RATE)))` with `VAT_RATE = 0.2`.

  PASS if the reported findings include a `Decision violated` (or clearly
  equivalent category name) finding citing decision 002 (by number, title
  or clearly described content) against fixtures/core/pricing.py, AND
  whose SUGGESTION (or ISSUE) names both ways out: changing the code to
  integer arithmetic, and recording a new or superseding decision in
  `.vibe/decisions/` if the float is wanted.
  FAIL if the decision is not reported as violated, or if the finding
  offers only one of the two ways out.
weight: 2
---

Reports the contradicted accepted decision and leaves the choice between
aligning the code and superseding the decision to the user.
