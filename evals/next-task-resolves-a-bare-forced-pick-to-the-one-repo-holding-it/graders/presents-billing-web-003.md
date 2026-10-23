---
type: llm
focus: last_message
criteria: |
  Only billing-web holds an item 003, so the bare number resolves to it.

  PASS if the message presents item 003 in billing-web as the pick awaiting
  confirmation.
  FAIL if it presents another item, reports 003 as not found, or asks which
  repo was meant instead of presenting the pick.
weight: 3
---

Resolves a bare number to the one active repo holding it.
