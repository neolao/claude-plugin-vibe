---
type: llm
focus: last_message
criteria: |
  The final message reports what the skill did.

  PASS if it does not present `orders-sdk` as a missing, gone, removed or
  archived repo, and does not say a question was raised about it (it may
  list it among the registered repos, or not mention it at all).
  FAIL if `orders-sdk` is reported as missing from the workspace, flagged
  as a discrepancy, removed, or archived.
weight: 1
---

An `idea` row is not a discrepancy: the report has nothing to flag about
it.
