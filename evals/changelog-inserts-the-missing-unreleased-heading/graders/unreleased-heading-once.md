---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\]"
match: count:1
weight: 2
---

Exactly one `## [Unreleased]` heading in the file: created when missing,
reused when present, never doubled.
