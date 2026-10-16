---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(empty|last page)"
flags: i
weight: 2
---

The unrelated fix between the feature and its revert still lands under
`### Fixed` inside `[Unreleased]`.
