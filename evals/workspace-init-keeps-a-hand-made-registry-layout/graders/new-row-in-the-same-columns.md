---
type: regex
target:
  source: file
  path: roadmap/repos.md
pattern: "\\|\\s*orders-web\\s*\\|[^|\\n]*\\|\\s*active\\s*\\|[^|\\n]*\\|[^|\\n]*\\|"
flags: ""
match: contains
weight: 2
---

`orders-web` (a new sibling with `.vibe/backlog/`) is added as a row
with five cells in the file's own column order — status in the third
column, as the header says — not as a four-cell template row.
