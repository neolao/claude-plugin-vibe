---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags the lock in `adjust_stock`
  (fixtures/inventory/api.py) as possibly never released: it is taken with
  `locks.hold(sku)` and released in a `finally`.
  A `Resource` finding on `sync_skus` in jobs.py does not count against this
  grader, even if it points at api.py as the pattern to follow or says the
  leaked lock blocks `adjust_stock`. Neither does a finding on the same
  function that the acquire has no timeout or blocks the event loop while it
  waits, nor one about the unawaited `audit.record`: those are not claims
  that `adjust_stock` itself fails to release the lock.
  PASS otherwise, including when the report has no finding at all.
weight: 1
---

Does not flag the `try`/`finally`-guarded lock in `adjust_stock`.
