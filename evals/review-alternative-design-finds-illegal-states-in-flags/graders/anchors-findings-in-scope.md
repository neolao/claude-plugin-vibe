---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/subscriptions/.

  PASS if every finding's FILE: line points to a file under
  fixtures/subscriptions/.
  FAIL if any finding is anchored on a file outside it.
weight: 1
---

Keeps every finding on the code under review.
