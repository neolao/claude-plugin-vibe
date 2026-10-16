---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Removed(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 3
---

The PDF export was released in 1.1.0 and reverted afterwards: the user
loses it, so the revert lands as a `### Removed` entry under
`[Unreleased]`.
