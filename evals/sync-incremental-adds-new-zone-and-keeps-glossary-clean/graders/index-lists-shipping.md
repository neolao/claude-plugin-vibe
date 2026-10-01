---
type: regex
pattern: 'modules/shipping\.md'
target: { source: file, path: ".vibe/index.md" }
match: contains
weight: 1
---

index.md must link the new module.
