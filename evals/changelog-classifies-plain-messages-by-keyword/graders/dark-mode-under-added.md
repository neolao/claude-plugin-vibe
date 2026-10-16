---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*dark"
flags: i
weight: 2
---

`Add dark mode to the report viewer` has no prefix; the `add` keyword
files it under `### Added`.
