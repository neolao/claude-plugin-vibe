---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(date|sort|order)"
flags: i
weight: 1
---

The sort-order fix is after every tag and goes under `### Fixed` inside
`[Unreleased]` whatever tag the range starts at.
