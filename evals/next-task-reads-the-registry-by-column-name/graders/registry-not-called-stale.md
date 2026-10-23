---
type: llm
focus: last_message
criteria: |
  Both repos named in the Repo column have their directory in the
  workspace, and no unlisted sibling exists: the registry is not stale,
  whatever order its columns come in.

  PASS if the message does not describe the registry as stale, out of date
  or in need of a refresh, and does not say that a listed repo is missing
  from the workspace.
  FAIL if it reports the registry as stale, says it scanned the siblings to
  fill a gap, or flags finance-team, platform-team, billing-api or
  legacy-batch as missing.
weight: 2
---

A reordered table is not a stale registry.
