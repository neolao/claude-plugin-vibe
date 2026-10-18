---
type: regex
target: trace
pattern: "depends_on:\\s*\\[[^\\]\\n]*002[^\\]\\n]*\\]"
weight: 3
---

The new item's frontmatter carries `depends_on: [002]`, per Step 7 — the
reference names an existing item, so it is recorded, not dropped. Neither
the fixture's items nor the skill's own template mention 002 in a
`depends_on`, so the only place this pattern can come from is the written
file.
