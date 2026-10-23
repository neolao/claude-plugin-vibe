---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:|vibe:end:"
match: not_contains
weight: 2
---

The answer given in the user's place is "none": no section is put under
management, so no marker pair appears in the hand-written README.
