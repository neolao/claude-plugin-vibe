---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(empty|last page)"
flags: i
weight: 1
---

The `fix:` commit lands under `### Fixed` inside `[Unreleased]`.
