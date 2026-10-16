---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 1
---

The `feat:` commit lands under `### Added` inside `[Unreleased]`.
