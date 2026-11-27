---
type: llm
focus: last_message
criteria: |
  fixtures/README.md opens `<!-- vibe:begin:docs-index -->` before its
  documentation list and never closes it: no `<!-- vibe:end:docs-index -->`
  follows, and fixtures/CLAUDE.md says the index sits between the two
  markers.

  PASS if the reported findings include a `Format` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/README.md and that says the `docs-index` begin marker has no
  matching end marker (or that the managed-section pair is left open).
  FAIL if no finding reports the unclosed marker.
weight: 2
---

Reports the managed-section marker pair left open: the one part of a
generator's shape the files themselves make checkable.
