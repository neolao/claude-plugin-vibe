---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\][\\s\\S]*### Fixed(?:(?!\\n##)[\\s\\S])*(empty|last page)"
flags: i
weight: 1
---

The fix lands under `### Fixed` inside `[Unreleased]`.
