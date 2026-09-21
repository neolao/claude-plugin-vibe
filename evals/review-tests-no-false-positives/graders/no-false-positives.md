---
type: llm
focus: last_message
criteria: |
  The fixtures use only clean, well-grounded test patterns that superficially
  resemble each checklist category without being a violation:
  - `test_reserve_deducts_from_stock` asserts a literal expected value (`7`)
    computed by hand from the fixture's starting stock, not re-derived via
    the same subtraction formula the implementation uses to actually decide
    correctness in a distinguishing way — a standard example-based
    assertion (not Tautological).
  - Both `InventoryService` error paths (non-positive quantity, insufficient
    stock) have dedicated, active tests using `assertRaises` (no Missing
    negative cases / Coverage gap).
  - `TestInventoryServiceIsolation` builds a fresh `InventoryService` per
    test in `setUp`, with no shared module-level mutable state (no
    Isolation issue).
  - `test_total_with_tax_applies_provided_rate` and
    `test_total_with_tax_rounds_to_cents` use a `Mock` only to isolate the
    external tax-rate lookup; the assertion checks `PricingService`'s own
    arithmetic combining the mocked rate with the subtotal, so it is not
    Over-mocked or Under-asserting, and the mocked collaborator does not
    make this an Implementation-coupled or Wrong-level test — it stays a
    fast, real-logic unit test.
  - All assertions use precise `assertEqual`/`assertRaises`, not broad
    matchers (no Assertion precision issue).
  - No test is skipped, commented out, or otherwise dead (no Dead test
    code), and nothing here depends on unavailable infrastructure (no
    Infrastructure issue).

  PASS if the response reports no `high` or `medium` severity finding in any
  of the review-tests categories on this code — either no findings at all,
  or only `low` severity style notes unrelated to these already-clean
  patterns. A `SUITE EXECUTED` header confirming the suite passed is
  expected and does not count as a finding.
  FAIL if it flags the literal expected values as tautological, invents a
  missing negative case or coverage gap where one already exists, calls the
  isolated per-test fixtures order-dependent, calls the pricing tests
  over-mocked/under-asserting/implementation-coupled/wrong-level, or flags
  the precise assertions as imprecise.
weight: 2
---

Does not invent test-quality findings on code that already follows the
clean pattern for each category.
