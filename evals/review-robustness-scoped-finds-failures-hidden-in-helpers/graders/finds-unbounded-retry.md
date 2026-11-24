---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Timeout/limit` (or clearly
  equivalent category name) finding on `fetch_invoice`
  (fixtures/billing/invoices.py) for calling `with_retries` without
  `attempts`: `with_retries` (fixtures/net/retry.py) defaults `attempts` to
  `None`, so while the billing API keeps failing it retries forever (with a
  fixed delay and no backoff) and the nightly reconciliation job never
  finishes. The finding may name the missing cap, the `None` default, the
  missing backoff, or several of them, as long as it says the retries are
  not capped.
  FAIL if no finding flags this call as retrying without a cap.
weight: 1
---

Reports the uncapped retry of the invoice fetch. invoices.py alone shows a
request with a 5-second timeout; only net/retry.py, outside the scope, shows
the retries never stop.
