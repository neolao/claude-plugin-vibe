---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 1
---

The PDF export landed after `v1.3.0-rc.1` and goes under `### Added`
inside `[Unreleased]`.
