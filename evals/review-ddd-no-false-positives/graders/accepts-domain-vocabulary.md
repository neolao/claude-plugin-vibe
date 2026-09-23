---
type: llm
focus: last_message
criteria: |
  The code uses `customer_id`, `Order`, `LineItem`, `Money` and "approval"
  throughout — the business's own words, consistently, with no second name
  for the same concept.

  PASS if the report contains no `high` or `medium` severity Ubiquitous
  language finding. A report with no findings at all passes.
  FAIL only if a Ubiquitous language finding is reported at high or medium
  severity.
weight: 1
---

Invents no vocabulary drift where one consistent name is used.
