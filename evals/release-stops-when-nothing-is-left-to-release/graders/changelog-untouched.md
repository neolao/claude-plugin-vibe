---
type: regex
pattern: '## \[Unreleased\]\s*## \[1\.2\.3\] - 2026-01-15'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 2
---

`CHANGELOG.md` still has its empty `[Unreleased]` heading directly above
`[1.2.3]`: no dated section was cut, and the CI commit earned no entry.
