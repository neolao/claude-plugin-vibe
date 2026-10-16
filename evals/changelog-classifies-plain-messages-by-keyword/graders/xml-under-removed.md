---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Removed(?:(?!\\n##)[\\s\\S])*XML"
flags: i
weight: 2
---

`Remove the legacy XML export` has no prefix; the `remove` keyword files
it under `### Removed`.
