---
type: regex
pattern: 'status:\s*blocked'
target: { source: file, path: ".vibe/backlog/002-add-monthly-summary.md" }
match: contains
weight: 2
---

A `blocked` verdict sets `status: blocked` in the item's frontmatter — it must
not be left `todo`, and must never have been moved to `in_progress` or `done`.
