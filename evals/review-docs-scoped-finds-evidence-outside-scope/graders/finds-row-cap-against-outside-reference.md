---
type: llm
focus: last_message
criteria: |
  fixtures/docs/guides/import.md says a CSV import is capped at 5 000
  rows; fixtures/docs/reference/limits.md, outside the scope, gives
  10 000 rows for the same limit, and fixtures/README.md names the
  reference pages as the authoritative source for every limit.

  PASS if the reported findings include a `Contradiction` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/docs/guides/import.md and whose ISSUE or SUGGESTION names the
  10 000 rows, `limits.md` or fixtures/docs/reference/limits.md as the
  other side.
  FAIL if no finding reports the two values of the row cap, or if the
  finding is anchored (its FILE: line) on fixtures/docs/reference/limits.md.
weight: 2
---

Reports the row cap the guide restates differently from the reference,
with the outside page as evidence: the other side of the contradiction
sits outside the scope and must be read there, and the finding stays
anchored on the guide.
