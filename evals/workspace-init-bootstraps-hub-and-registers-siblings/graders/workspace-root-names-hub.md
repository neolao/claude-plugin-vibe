---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "## Hub repo\\n`roadmap/`"
flags: ""
match: contains
weight: 1
---

The workspace-root `CLAUDE.md` has a `## Hub repo` line naming `roadmap/`
exactly — this is the pointer Step 2 and `/vibe:next-task` read back on a
later run.
