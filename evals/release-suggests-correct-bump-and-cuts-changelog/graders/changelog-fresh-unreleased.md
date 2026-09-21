---
type: regex
pattern: '## \[Unreleased\]\s*## \[1\.2\.4\]'
target: { source: file, path: "CHANGELOG.md" }
match: contains
weight: 1
---

A fresh, empty `## [Unreleased]` section sits directly above the new
`## [1.2.4]` section — nothing but whitespace between the two headings,
proving the Fixed entries moved out of Unreleased rather than being
duplicated.
