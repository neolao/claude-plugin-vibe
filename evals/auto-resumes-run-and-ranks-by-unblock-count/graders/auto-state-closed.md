---
type: regex
pattern: "status:\\s*idle"
target: { source: file, path: ".vibe/auto-state.md" }
weight: 1
---

Step 5 closes the run: the journal's frontmatter reads `status: idle` again,
so the next `/vibe:auto` starts a fresh run instead of resuming this one.
