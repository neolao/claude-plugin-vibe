---
type: tool_order
before:
  tool: Edit
  input_match: "types/roster\\.contract\\.json"
after:
  tool: Bash
  input_match: "git commit"
weight: 2
---

Deterministic red-before-green-before-commit check: the contract fix that
makes the build pass must land before the final commit, not after — the
task cannot reach Commit on a broken build.
