---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "revert"
flags: i
match: not_contains
weight: 1
---

The commit's `Revert "…"` subject is history, not a change: the word has
no place in the file.
