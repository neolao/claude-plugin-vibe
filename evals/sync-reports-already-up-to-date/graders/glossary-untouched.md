---
type: regex
pattern: '##\s+Session'
target: { source: file, path: ".vibe/glossary.md" }
match: contains
weight: 1
---

`Session`'s cited source exists and nothing changed, so the self-cleaning pass
must not remove or rewrite the entry — it must not run at all.
