---
type: regex
target: last_message
pattern: "1\\s+item(?:\\(s\\))?\\s+done"
flags: i
weight: 1
---

Reports exactly one item done (from `done/000-qux.md`), per the "N item(s)
done — see `.vibe/backlog/done/`." line in Step 2.
