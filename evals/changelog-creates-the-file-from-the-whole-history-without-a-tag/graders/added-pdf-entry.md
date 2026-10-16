---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\][\\s\\S]*### Added(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 2
---

The feature lands under `### Added` inside `[Unreleased]`.
