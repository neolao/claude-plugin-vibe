---
type: llm
focus: last_message
criteria: |
  The brief says a handful of accounts already show two active
  subscriptions. A unique index or constraint over the active rows cannot
  be created while those duplicates exist: the migration would fail.

  PASS if the reply (REQUIREMENTS, RISKS or TEST SCENARIOS) says the
  existing accounts with two active subscriptions must be found and
  resolved (one of the two cancelled, merged, or otherwise made to comply)
  before the database constraint is created, or that creating the
  constraint fails until they are. Leaving the choice of which subscription
  to keep to the Product Owner passes.
  FAIL if the reply prescribes the database constraint without saying
  anything about the accounts that already hold two active subscriptions,
  or if it has no such constraint at all.
weight: 2
---

Deals with the accounts that already break the rule before the constraint
that forbids it is created.
