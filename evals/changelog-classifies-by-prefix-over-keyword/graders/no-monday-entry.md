---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "Monday"
match: not_contains
weight: 1
---

The commit's own wording says nothing to the user and must not be copied
into the file.
