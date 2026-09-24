---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 1
---

The scoped `feat(export): add PDF export for monthly reports` commit lands
under `### Added` inside `[Unreleased]`.
