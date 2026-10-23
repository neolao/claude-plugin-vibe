---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:|vibe:end:"
match: not_contains
weight: 3
---

A hand-written README never receives marker pairs silently: the skill
asks first, and the question goes unanswered in this case.
