---
type: llm
focus: last_message
criteria: |
  The worker marks the order as refunded and emails the customer after
  the provider's API accepts the call; a call that reached the sandbox,
  or any provider response that is not a confirmed refund, must not mark
  the order nor email the customer.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS says, in any wording,
  that the order is marked refunded and the customer emailed only on a
  confirmed refund from the live provider — a successful response, a
  refund id stored on the order, a check that the configured endpoint is
  the live one — or names, as a risk or a scenario, the refund marked
  and the customer emailed while no money moved.
  FAIL if the reply never connects the provider's response (or the
  endpoint it reached) to whether the order is marked and the customer
  emailed.
weight: 1
---

Ties marking the order and emailing the customer to a confirmed refund
from the live provider, so a call that reached the wrong endpoint moves
no order.
