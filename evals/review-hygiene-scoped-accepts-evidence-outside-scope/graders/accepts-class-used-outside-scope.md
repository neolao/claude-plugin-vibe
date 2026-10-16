---
type: llm
focus: last_message
criteria: |
  `InvoiceNumberSequence` in fixtures/billing/numbering.py is instantiated
  nowhere inside the scope (fixtures/billing/), but
  fixtures/workers/nightly.py imports it (via the `billing` package) and
  uses `next()` and `last_issued()`.

  PASS if no `high` or `medium` severity finding calls
  `InvoiceNumberSequence`, or any of its methods, dead or unused code. A
  report with no findings at all passes.
  FAIL if the class or one of its methods is flagged as Dead code (or
  equivalent) at high or medium severity.
weight: 1
---

Does not call a class dead when its only user sits outside the path under
review.
