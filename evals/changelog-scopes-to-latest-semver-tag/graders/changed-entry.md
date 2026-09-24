---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Changed(?:(?!\\n##)[\\s\\S])*report list"
flags: i
weight: 1
---

The `improve: load the report list twice as fast on large accounts` commit,
reached through a merged branch, lands under `### Changed` inside
`[Unreleased]`.
