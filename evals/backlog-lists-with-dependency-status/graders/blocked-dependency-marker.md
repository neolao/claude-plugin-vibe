---
type: regex
target: last_message
pattern: "002[^\\n]*⚠[^\\n]*001"
weight: 2
---

The `002` row shows the `⚠` marker naming `001` as its unmet dependency, per
the skill's Step 2 table format.
