---
type: llm
focus: last_message
criteria: |
  The kept finding about the threshold boundary (pricing.py:8, `>` instead
  of `>=`): the code tries to meet the requirement and gets the bound wrong.
  The need is understood, the execution is wrong.

  PASS if that finding is classified `high` and in the `implementation`
  space (written `(high · implementation)` or equivalent wording with both
  values), with a **Consequence:** sentence naming the customer who spent
  exactly 500 and gets no discount.
  FAIL if it is routed to the `need` space, if it is below `high`, or if the
  consequence is hedged ("could", "in theory") or absent.
weight: 2
---

A wrong bound on a requirement the code does try to meet is an
implementation finding, high because customers are charged wrongly.
