---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(date|sort|order)"
flags: i
weight: 1
---

The sort-order fix is the only commit since `v1.1.0` and goes under
`### Fixed` inside `[Unreleased]`.
