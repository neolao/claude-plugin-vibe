---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "ruff check"
flags: i
match: contains
weight: 1
---

The regenerated CLAUDE.md reflects the real lint command detected from
`pyproject.toml` (`ruff check ...`), not the stale "no linter configured"
note left over from the prior run.
