---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Leftover` (or clearly equivalent
  category name, such as `Dead code`) finding on the `order_total` local in
  `refund_amount` (fixtures/billing/refunds.py), which is computed and then
  never read.
  FAIL if no finding flags `order_total` as unused.
weight: 1
---

Reports the unused `order_total` variable in fixtures/billing/refunds.py's
`refund_amount`. A reader can take it for a cap on the refund that the code
never applies, so it carries a cost under the contract's "plausible failure
or cost" filter — unlike an unused stdlib import, which the sonnet agent
consistently judged not worth a finding.
