---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Deprecated(?:(?!\\n##)[\\s\\S])*/v1/reports"
weight: 3
---

The deprecated endpoint is the user's own call site: the `### Deprecated`
entry under `[Unreleased]` must say `/v1/reports`, with or without
backticks.
