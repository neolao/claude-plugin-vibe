---
type: regex
pattern: 'status:\s*blocked'
target: { source: file, path: ".vibe/backlog/003-add-last-of.md" }
match: contains
weight: 2
---

Incrementing `attempt` takes 003 from 2 to 3, above the cap of 2: Step 0 marks
the item `blocked` in its own frontmatter instead of re-running it.
