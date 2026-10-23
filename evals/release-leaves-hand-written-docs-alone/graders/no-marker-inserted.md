---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:|vibe:end:"
match: not_contains
weight: 1
---

No marker pair appears in the hand-written README.
