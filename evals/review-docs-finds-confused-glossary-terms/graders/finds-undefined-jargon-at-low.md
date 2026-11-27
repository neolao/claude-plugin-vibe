---
type: llm
focus: last_message
criteria: |
  "settlement batch" is used in fixtures/docs/import.md,
  fixtures/docs/export.md and fixtures/docs/review.md; .vibe/glossary.md
  has no entry for it.

  PASS if the reported findings include a `Vocabulary` (or clearly
  equivalent category name) finding with SEVERITY `low` that names
  "settlement batch" as a recurring term with no glossary entry and gives
  the number of docs (or files) it appears in.
  FAIL if no finding names "settlement batch", if the finding is rated
  `medium` or `high`, or if it gives no count of docs.
weight: 1
---

Reports the recurring undefined term at `low` with its spread: whether
it deserves an entry is not the agent's call, the count is.
