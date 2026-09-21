---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "### Removed[\\s\\S]{0,500}(XML|xml)"
weight: 1
---

The `remove: drop the legacy XML export format` commit lands under
`### Removed` in `[Unreleased]`.
