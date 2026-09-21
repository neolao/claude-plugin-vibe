---
type: llm
focus: last_message
criteria: |
  The code uses `customer_id`, `Order`, `Money` and "approval" throughout —
  the business's own words, consistently, with no second name for the same
  concept.

  PASS if no `high` or `medium` severity Ubiquitous language finding is
  reported.
  FAIL if one is.
weight: 1
---

Invents no vocabulary drift where one consistent name is used.
