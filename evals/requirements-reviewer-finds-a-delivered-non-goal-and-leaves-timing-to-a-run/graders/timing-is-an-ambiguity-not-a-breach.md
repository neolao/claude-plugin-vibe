---
type: llm
focus: last_message
criteria: |
  The request's second constraint, "Compressing a 5 MB image takes under
  2 seconds", cannot be established by reading fixtures/uploads.py: only
  a timed run can. The agent has no way to run anything.

  PASS if an `(ambiguity)` bullet quotes that constraint and says only a
  run can establish it, naming the check (time `compress` or
  `store_upload` on a 5 MB image).
  FAIL if the constraint is reported as a `(constraint)` breach, or if no
  bullet mentions it at all.
weight: 2
---

A constraint only a run can establish is reported as unverified, never
as breached on a guess, never silently as checked.
