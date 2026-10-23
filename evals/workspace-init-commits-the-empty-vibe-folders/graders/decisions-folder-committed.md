---
type: regex
pattern: '\.vibe/decisions/\.gitkeep'
target: last_message
match: contains
weight: 2
---

`git -C roadmap ls-files .vibe` lists `.vibe/decisions/.gitkeep`: the
empty decisions folder is in the hub's history too.
