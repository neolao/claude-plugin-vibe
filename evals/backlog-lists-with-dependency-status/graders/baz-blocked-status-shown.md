---
type: regex
target: last_message
pattern: "003[^\\n]*blocked"
flags: i
weight: 2
---

The `003` row (or its surrounding text) reports its `blocked` status.
