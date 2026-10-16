---
type: regex
target: last_message
pattern: "002[^\\n]*⚠[^\\n]*009[^\\n]*missing"
flags: i
weight: 3
---

The `002` row shows `009` with the `⚠` marker and the word "missing", per
Step 2: no item 009 exists at the top level or under `done/`.
