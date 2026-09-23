---
type: regex
target: last_message
pattern: "AUTO-RESULT:\\s*done"
flags: i
weight: 2
---

Once the build gate is satisfied, nothing else in this fixture should
legitimately block or abort the run — the final report must end with
`done`, not `blocked` or `aborted`.
