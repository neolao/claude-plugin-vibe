---
type: regex
pattern: '##\s+Session'
target: { source: file, path: ".vibe/glossary.md" }
match: contains
weight: 1
---

`Session` is a real domain concept whose source `src/auth/index.js` exists and
was just extended. Self-cleaning must not take it with the orphaned entry.
