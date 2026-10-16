---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\][\\s\\S]*## \\[1\\.0\\.0\\]"
weight: 2
---

The new heading goes where Keep a Changelog puts it: above the first
version section, not at the end of the file.
