---
type: llm
focus: last_message
criteria: |
  fixtures/docs/import.md carries `<!-- KEEP IN SYNC with docs/limit.md -->`
  above its row-cap paragraph; the file that exists is
  fixtures/docs/limits.md, and no docs/limit.md exists.

  PASS if the reported findings include a `Dangling reference` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/docs/import.md and that names the KEEP IN SYNC marker (or
  `docs/limit.md`) as pointing to a file that does not exist.
  FAIL if no finding reports the marker's target.
weight: 2
---

Reports the sync marker whose named counterpart does not exist: the
block it guards can no longer be compared with anything.
