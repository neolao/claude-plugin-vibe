---
type: llm
focus: last_message
criteria: |
  The working directory has a `CLAUDE.md` with a `## Hub repo` line, and
  `hub/` carries the marker (`.git/` plus `repos.md`) listing two active
  repos.

  PASS if the presentation shows the workspace scope at work: the pick and
  the items it did not choose come from more than one repo of the registry
  (orders-sdk and orders-api), or the message says outright that it is in
  workspace scope. It does not have to use the words "workspace scope".
  FAIL if it reports mono-repo scope, says no workspace was detected, or
  only discusses items of a single repo.
weight: 2
---

Detects workspace scope from the hub marker.
