---
type: llm
focus: last_message
criteria: |
  The working directory has a `CLAUDE.md` with a `## Hub repo` line, and
  `hub/` carries the marker (`.git/` plus `repos.md`) listing two active
  repos.

  PASS if the skill states it is working in workspace scope — candidates come
  from the sibling repos in the registry — rather than mono-repo scope or no
  workspace at all.
  FAIL if it reports mono-repo scope, or says no workspace was detected.
weight: 2
---

Detects workspace scope from the hub marker.
