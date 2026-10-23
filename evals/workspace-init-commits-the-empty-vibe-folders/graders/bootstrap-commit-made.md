---
type: llm
focus: trace
criteria: |
  Look at every Bash tool call and its output (git commands in particular).

  PASS only if some commit was made inside the `roadmap/` hub repo
  (working directory `roadmap` or a `git -C roadmap ...` invocation)
  whose subject line is or starts with "chore: bootstrap hub repo".
  FAIL if no such commit was made, or if the top-level workspace-root
  `CLAUDE.md` (next to `roadmap/`, not `roadmap/CLAUDE.md`) was ever
  added to or committed in any repo.
weight: 1
---

The bootstrap ends with the hub's own commit, and the workspace-root
`CLAUDE.md` stays local-only.
