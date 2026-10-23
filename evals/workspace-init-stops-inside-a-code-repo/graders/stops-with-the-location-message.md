---
type: llm
focus: last_message
criteria: |
  The final message reports what the skill did and said.

  PASS if it says the skill stopped because it was run from inside a repo
  (not from the workspace root), and relays an instruction to run it from
  the workspace root (the parent folder) or from the hub repo — and does
  not claim that a hub repo, a `repos.md` or a workspace-root `CLAUDE.md`
  was created or refreshed.
  FAIL if the message reports a hub bootstrapped, a registry written, a
  commit made, or says nothing about where the command must be run from.
weight: 2
---

From inside a code repo, the skill's only output is the Step 1 stop
message pointing at the workspace root.
