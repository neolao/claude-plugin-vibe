---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Fixed(?:(?!\\n##)[\\s\\S])*(session|logout|log out|signed in|logged in)"
flags: i
weight: 2
---

`fix: remove stale sessions that kept users signed in after logout` is a
bug fix: the `fix:` prefix decides, and the entry lands under `### Fixed`.
