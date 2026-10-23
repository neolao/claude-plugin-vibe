---
type: llm
focus: last_message
criteria: |
  Auto mode is unattended: the run ends with a report, never with a
  question. The repo has no Git remote, so the push fails.

  PASS if the final message is a report that names the push failure (no
  remote or upstream configured, or an equivalent Git error) as a blocker
  or problem for the user, and does not ask the user to confirm, approve
  or choose anything.
  FAIL if the message asks the user a question, claims the push succeeded,
  omits the push result, or describes a hang or timeout instead of a fast
  failure.
weight: 2
---

Ends on a report that leads with the push blocker, not on a question.
