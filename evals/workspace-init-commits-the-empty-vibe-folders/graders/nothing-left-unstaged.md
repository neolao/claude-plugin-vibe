---
type: regex
pattern: 'porcelain-lines\|0'
target: last_message
match: contains
weight: 2
---

`git status --porcelain` of the hub prints no line after the run:
everything the run wrote — registry, `.vibe/`, `CLAUDE.md`, what
`vibe:docs` and `vibe:sync` produced — went into the bootstrap commit.
