---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*(two.factor|2FA|second factor)"
flags: i
weight: 2
---

`feat: add two-factor auth to the login page` is a feature: the `feat:`
prefix decides, and the entry lands under `### Added`.
