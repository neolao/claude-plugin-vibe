---
type: llm
focus: last_message
criteria: |
  `SubscriptionResponse` in fixtures/api/presenters.py is the shape the
  account page reads, filled by `to_response` from a `Subscription` and never
  written back; `GatewayPayment` and `InvoiceSummary` in
  fixtures/billing/invoice_summary.py are the gateway's export row and the
  statement line, and `summarize` works the export row's fields. None of
  them is a domain type with an identity.

  PASS if no `high` or `medium` severity Anemic model, Value object or
  Domain service finding targets `SubscriptionResponse`, `to_response`,
  `GatewayPayment`, `InvoiceSummary` or `summarize` — for being a data bag,
  for a function working their fields from outside, or for their bare
  integer cents. A report with no findings at all passes.
  FAIL if one of them is flagged for one of those reasons at high or medium
  severity.
weight: 1
---

Leaves boundary shapes and the functions that work them alone: a DTO is
data by design, and envy of a non-domain object is review-antipatterns'.
