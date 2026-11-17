---
type: llm
focus: last_message
criteria: |
  A plan change cancels the current subscription and starts a new one. If
  the two writes are separate, a failure between them leaves the account
  with no active subscription, or with two.

  PASS if REQUIREMENTS requires the cancellation of the current
  subscription and the insertion of the new one to happen in one database
  transaction (any order that keeps the one-active rule satisfied, or a
  deferred constraint, passes).
  FAIL if the reply does not require the two writes of a plan change to
  succeed or fail together, or only mentions it in RISKS or TEST SCENARIOS.
weight: 2
---

Keeps the cancel and the insert of a plan change in one transaction.
