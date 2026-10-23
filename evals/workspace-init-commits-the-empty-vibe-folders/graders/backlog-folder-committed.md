---
type: regex
pattern: '\.vibe/backlog/\.gitkeep'
target: last_message
match: contains
weight: 2
---

`git -C roadmap ls-files .vibe` lists `.vibe/backlog/.gitkeep`: the
empty backlog folder is in the hub's history, so a clone has it.
