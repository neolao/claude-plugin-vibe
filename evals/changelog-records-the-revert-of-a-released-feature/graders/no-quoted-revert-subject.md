---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "Revert \""
match: not_contains
weight: 1
---

The entry is the user-facing effect, not the commit subject copied with
its quotes.
