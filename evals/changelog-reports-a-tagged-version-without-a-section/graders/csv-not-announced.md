---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*CSV"
flags: i
match: not_contains
weight: 2
---

The CSV export is tagged `v1.1.0`: it is released and lies before the
range, so it never reaches `[Unreleased]`.
