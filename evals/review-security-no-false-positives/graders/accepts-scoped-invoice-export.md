---
type: llm
focus: last_message
criteria: |
  `export_invoices` scopes its query to the caller's own customer with
  `WHERE customer_id = ?`, so the `requesting_user` argument does decide what
  comes back.

  PASS if no finding claims this function is missing an authorization or
  access-control check.
  FAIL if it is flagged as missing access control.
weight: 1
---

Does not invent a missing access-control check on the scoped invoice export.
