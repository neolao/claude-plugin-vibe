---
type: llm
focus: last_message
criteria: |
  PASS if the response's `E2E/INTEGRATION EXECUTED:` line (or the findings
  right after it) says the e2e suite was run (`npm run test:e2e` or
  `node --test e2e/...`) and that it FAILED, naming the bulk-order test in
  fixtures/e2e/checkout.test.js (expected 1620, got a negative total such
  as -16200) — while the unit suite passed.
  FAIL if the e2e suite is reported as not run, as passing, or its failure
  is not mentioned.
weight: 2
---

Runs the separate e2e script and reports its failing bulk-order test.
