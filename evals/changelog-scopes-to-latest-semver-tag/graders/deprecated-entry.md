---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Deprecated(?:(?!\\n##)[\\s\\S])*v1"
flags: i
weight: 1
---

The `deprecate: mark the /v1/reports endpoint as deprecated in favour of
/v2/reports` commit lands under `### Deprecated` inside `[Unreleased]`.
