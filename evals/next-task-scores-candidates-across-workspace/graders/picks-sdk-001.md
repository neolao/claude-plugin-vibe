---
type: llm
focus: last_message
criteria: |
  Two candidates are unblocked: orders-sdk 001 (orders-api 002's notes wait on
  `orders-sdk#001`) and orders-sdk 002 (nothing waits on it). Step 5 ranks by
  the number of items unblocked first.

  PASS if the presented pick is item 001 in orders-sdk.
  FAIL if it picks orders-sdk 002, either orders-api item, or the hub item.
weight: 3
---

Picks the candidate that unblocks another repo's item.
