---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 2
---

The PDF export landed after the release commit and is covered nowhere:
it goes under `### Added` inside `[Unreleased]`.
