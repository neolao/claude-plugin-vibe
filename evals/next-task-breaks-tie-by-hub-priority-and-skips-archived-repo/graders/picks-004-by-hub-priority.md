---
type: llm
focus: last_message
criteria: |
  billing-api 001 and billing-api 004 each unblock exactly one item
  (billing-web 003 and 004 wait on them). Step 5 then falls to the hub
  decision, which names billing-api#004 first, before the lowest number.

  PASS if the presented pick is item 004 in billing-api.
  FAIL if it picks billing-api 001, any other item, or an item of
  legacy-batch.
weight: 3
---

Breaks the unblock-count tie with the hub decision.
