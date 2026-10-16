---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(date|sort|order)"
flags: i
weight: 1
---

The sort-order fix landed after the release commit and is covered
nowhere: it goes under `### Fixed` inside `[Unreleased]`.
