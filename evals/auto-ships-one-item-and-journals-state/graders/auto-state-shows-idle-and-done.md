---
type: regex
target:
  source: file
  path: .vibe/auto-state.md
pattern: "status:\\s*idle[\\s\\S]*-\\s*001[^\\n]*done"
weight: 2
---

By Step 5 the run journal's frontmatter must read `status: idle` (the run
closed cleanly) and the journal body must carry item 001's line marked
`done`, in that order (frontmatter first, journal entries after).
