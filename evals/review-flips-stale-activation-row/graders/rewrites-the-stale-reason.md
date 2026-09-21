---
type: regex
target: { source: file, path: "CLAUDE.md" }
pattern: "no HTTP surface in this project"
match: not_contains
weight: 1
---

Flipping the row is only half of Step 1: the stale reason must be rewritten
too, so the table stops asserting something the code contradicts.
