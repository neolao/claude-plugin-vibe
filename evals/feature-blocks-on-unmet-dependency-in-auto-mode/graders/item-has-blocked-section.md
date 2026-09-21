---
type: regex
pattern: '##\s+Blocked'
target: { source: file, path: ".vibe/backlog/002-add-monthly-summary.md" }
match: contains
weight: 1
---

The verdict is recorded in the file itself: a `## Blocked` section with the
date and the one-line reason, so a later run knows why it stopped.
