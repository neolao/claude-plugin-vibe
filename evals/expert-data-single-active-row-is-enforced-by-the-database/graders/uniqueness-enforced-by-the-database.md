---
type: llm
focus: last_message
criteria: |
  The brief says an account may have one active subscription, and that the
  signup handler checks for an active one before inserting. A check in the
  application followed by an insert lets two concurrent requests both see
  no active row and both insert. The expert's checklist says a uniqueness
  the data needs left to the application stays a defect.

  PASS if REQUIREMENTS requires the database itself to guarantee at most one
  active subscription per account — a partial unique index or constraint on
  `account_id` limited to the rows where `cancelled_at` is empty, an
  exclusion constraint, or an equivalent database-enforced rule.
  FAIL if the one-active-subscription rule stays enforced only by the
  application (its existing check, a retry, a lock taken in application
  code, a `SELECT … FOR UPDATE` without a constraint), or if a constraint
  is only suggested in RISKS or as an option.
weight: 2
---

Requires the one-active-subscription rule to be enforced by the database,
not only by the signup handler's check.
