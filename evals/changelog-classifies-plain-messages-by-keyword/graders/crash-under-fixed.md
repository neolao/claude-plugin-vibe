---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(no rows|empty|crash)"
flags: i
weight: 2
---

`Patch the crash when a report has no rows` has no prefix; the `patch`
keyword files it under `### Fixed`.
