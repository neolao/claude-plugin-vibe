---
type: llm
focus: last_message
criteria: |
  fixtures/README.md, outside the scope, is the index of docs/: it lists
  fixtures/docs/guides/import.md and the three reference pages, and never
  lists fixtures/docs/guides/export.md.

  PASS if the reported findings include an `Index drift` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/docs/guides/export.md and whose ISSUE or SUGGESTION names
  README.md (or "the index") as the place that omits it.
  FAIL if no finding reports that export.md is missing from the index, or
  if the finding is anchored (its FILE: line) on fixtures/README.md.
weight: 2
---

Reports the guide the outside index omits, anchored on the guide: the
index is outside the scope, so it is named as the place to fix, never
used as the anchor.
