---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 2
---

The PDF export is the commit that `deploy-2026-10-30` and `vnext` point
at: a range starting at the lexically or version-sorted latest tag leaves
it out. It goes under `### Added` inside `[Unreleased]`.
