---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "### Security[\\s\\S]{0,500}(sanitiz|injection)"
flags: i
weight: 1
---

The `security: sanitize user input in the search endpoint to prevent
injection` commit lands under `### Security` in `[Unreleased]`.
