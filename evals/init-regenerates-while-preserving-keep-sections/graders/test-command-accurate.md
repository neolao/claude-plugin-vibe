---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "pytest"
flags: i
match: contains
weight: 1
---

The regenerated CLAUDE.md reflects the real test command detected from
`pyproject.toml` (`pytest`, via `[tool.poe.tasks]`), not the stale
`python -m unittest` command left over from the prior run.
