---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\]"
match: count:1
weight: 1
---

Exactly one `## [Unreleased]` heading.
