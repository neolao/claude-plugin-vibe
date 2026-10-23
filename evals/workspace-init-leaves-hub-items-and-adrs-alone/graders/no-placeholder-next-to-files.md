---
type: regex
pattern: '\.vibe/(backlog|decisions)/\.gitkeep'
target: last_message
match: not_contains
weight: 1
---

`git -C roadmap ls-files .vibe` lists no `.gitkeep` in either folder:
the placeholder is for an empty folder, and both hold a file already.
