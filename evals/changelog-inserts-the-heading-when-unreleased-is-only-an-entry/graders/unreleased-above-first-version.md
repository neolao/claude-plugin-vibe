---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\][\\s\\S]*## \\[1\\.0\\.0\\]"
weight: 2
---

The new heading goes above the first version section, not at the end of
the file and not under the entry that happens to say "unreleased".
