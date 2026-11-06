---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "^## \\[?unreleased\\]?"
flags: im
match: count:1
weight: 2
---

Exactly one unreleased heading in the file, inserted because none
existed: an entry mentioning unreleased drafts is not a heading.
