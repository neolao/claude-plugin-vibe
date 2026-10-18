---
type: llm
focus: last_message
criteria: |
  Finding 3 (review-robustness, a `None` total raising in `apply_discount`)
  is false: `apply_discount` returns `None` when `total is None`
  (fixtures/pricing.py:14-15), before any multiplication.

  PASS if finding 3 appears under `## DISCARDED` with a **Dropped:** reason
  that points at the `total is None` guard in `apply_discount` (line 14 or
  15, or the guard quoted).
  FAIL if finding 3 is kept under `## CLASSIFIED findings` at any level, or
  if it is dropped for a reason that does not cite the guard.
weight: 2
---

Drops the false positive, and anchors the reason in the source rather than
in the finding's own text.
