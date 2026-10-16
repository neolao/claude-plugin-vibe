---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*PDF"
flags: i
match: not_contains
weight: 3
---

The PDF export was added and reverted since the last tag: the user never
gets it. The entry the feature had written under `[Unreleased]` must be
gone, and no new one may describe the export or its removal.
