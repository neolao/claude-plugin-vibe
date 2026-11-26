---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(?:page|list)"
flags: i
weight: 2
---

The fix to the released pagination (an empty report list now shows an empty
first page) is listed under `### Fixed` in `## [Unreleased]`.
