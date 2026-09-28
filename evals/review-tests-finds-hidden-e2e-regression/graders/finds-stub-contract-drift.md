---
type: llm
focus: last_message
criteria: |
  PASS if a finding targets the `pricing` stub in fixtures/test/cart.test.js
  and explains that its `discountFor` returns a fraction (`0.1`) while the
  real `discountFor` in fixtures/src/pricing.js returns a percent (`10`), so
  the unit test passes on a contract the real collaborator does not honour
  and hides the broken total the e2e run exposes. Any category fits
  (`Over-mocked`, `Wrong level`, `Tautological`…) as long as the finding
  names that fraction-vs-percent mismatch.
  FAIL if no finding points out that the stub's discount unit disagrees
  with the real pricing module.
weight: 2
---

Traces the e2e failure to a unit-test stub that disagrees with the real
collaborator.
