---
type: regex
pattern: '##\s+([Rr]etry\s*[Bb]uffer|[Aa]xios)'
target: { source: file, path: ".vibe/glossary.md" }
match: not_contains
weight: 2
---

A response buffer and an HTTP client are plumbing, not business concepts; Step 4 excludes them.
