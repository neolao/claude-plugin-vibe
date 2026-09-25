---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "Lint exits 0 \\(`(poe lint|ruff check[^`]*)`\\)"
flags: ""
match: contains
weight: 1
---

The Definition of Done's lint line names the real lint command detected from
`pyproject.toml` — the `poe lint` task, or the `ruff check ...` it runs —
not the stale `n/a` left over from the prior run.
