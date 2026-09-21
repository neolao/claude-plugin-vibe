---
type: regex
target: files
pattern: "^\\.vibe/backlog/(001|002|003)-[a-z0-9-]+\\.md$"
flags: m
match: "count:3"
weight: 2
---

Exactly three new backlog item files were created, numbered `001`, `002`,
and `003` (numbering starts at 1 since the fixture's `.vibe/backlog/` is
empty) — not fewer, not more, and not misnumbered.
