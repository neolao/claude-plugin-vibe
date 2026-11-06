---
type: llm
focus: last_message
criteria: |
  The brief leaves two things open that only the product can settle:
  whether more promotion kinds are coming (marketing "has ideas"), and
  whether the coupon and the promotion combine on one cart. The expert's
  rule: when the choice rests on what the product will do next, ask that
  as the one question the choice depends on, phrased for a non-technical
  Product Owner, and say which option each answer picks.

  PASS if OPEN QUESTIONS contains at least one question about the
  product's rules or future — whether or roughly how many more promotion
  kinds are planned, or whether the coupon and the promotion may apply
  together and which wins — written in plain words a non-technical Product
  Owner can answer, and the reply says which option that answer leads to
  (or how the answer changes the recommendation).
  FAIL if the reply has no OPEN QUESTIONS, if none of its questions is
  about the product's rules or future, or if no question is tied to the
  option it would pick.
weight: 2
---

Asks the Product Owner the product question the design choice depends on,
and ties each answer to the option it picks.
