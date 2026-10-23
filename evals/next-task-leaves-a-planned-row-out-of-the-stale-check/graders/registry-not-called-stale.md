---
type: llm
focus: last_message
criteria: |
  billing-sdk is listed `planned` in repos.md: a planned repo has no
  directory yet, by definition. Nothing in the workspace is missing or
  unlisted, so the registry is not stale.

  PASS if the message does not describe the registry as stale, out of date
  or in need of a refresh, and does not present billing-sdk as a missing or
  gone repo (it may mention billing-sdk as planned, or not at all).
  FAIL if it reports the registry as stale, says it scanned the siblings to
  fill a gap, or flags billing-sdk as missing from the workspace.
weight: 2
---

A planned row without a directory is not a discrepancy.
