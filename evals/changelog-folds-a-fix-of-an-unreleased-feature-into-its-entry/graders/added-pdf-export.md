---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
weight: 2
---

The PDF export is listed under `### Added` in `## [Unreleased]`.
