---
type: llm
focus: last_message
criteria: |
  `freezegun` is declared in the `dev` extra of fixtures/pyproject.toml and
  imported only by fixtures/tests/test_pricing.py, outside the scope
  (fixtures/orders/): it is used, and declared in the right section.

  PASS if no `high` or `medium` severity `Unused` or `Misplaced` finding
  targets `freezegun`. A report whose only finding says the audit tool
  could not run passes.
  FAIL if `freezegun` is flagged as unused or misplaced at high or medium
  severity.
weight: 1
---

Does not call a dev-extra package unused or misplaced when the test that
imports it sits outside the path under review.
