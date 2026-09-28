---
type: llm
focus: last_message
criteria: |
  The pricing tests mock only the external tax-rate lookup, keyed by region
  (`side_effect = {"US": 0.2}.__getitem__`), so an implementation that
  ignores or garbles the region raises `KeyError`; the assertions check
  `PricingService`'s own arithmetic combining that rate with the subtotal,
  so a wrong `total_with_tax` fails them.

  PASS if no `high` or `medium` severity Over-mocked, Under-asserting,
  Implementation-coupled, or Wrong level finding targets them.
  FAIL if any does at high or medium severity.
weight: 1
---

Does not call a narrowly mocked collaborator over-mocking.
