---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "^## \\[?unreleased\\]?"
flags: im
match: count:1
weight: 3
---

Exactly one unreleased heading, whatever its spelling: the existing
`## Unreleased` is reused, no `## [Unreleased]` is added next to it.
