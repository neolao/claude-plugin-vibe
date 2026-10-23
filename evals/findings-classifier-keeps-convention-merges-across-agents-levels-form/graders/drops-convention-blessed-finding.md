---
type: llm
focus: last_message
criteria: |
  Finding 1 (review-robustness, a broad `Exception` catch in `get_notes`)
  describes what `fixtures/CONVENTIONS.md` prescribes: handlers catch
  `Exception` once, at their outermost function, and return a 500.

  PASS if finding 1 appears under `## DISCARDED` with a **Dropped:** reason
  that cites the project convention (the conventions file, or its rule
  quoted).
  FAIL if finding 1 is kept under `## CLASSIFIED findings` at any level, or
  if it is dropped for a reason that does not cite the convention.
weight: 2
---

The convention is a source in the working directory; the classifier must read
it, not trust the finding.
