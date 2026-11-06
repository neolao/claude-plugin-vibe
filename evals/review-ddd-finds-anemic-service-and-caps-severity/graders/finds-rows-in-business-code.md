---
type: llm
focus: last_message
criteria: |
  `SubscriptionRepository.find_expiring` in
  fixtures/subscriptions/subscription_repository.py returns the raw
  `fetchall()` rows of a SQL join, and `expiry_notices` in
  fixtures/billing/expiry_notices.py reads them by index (`row[5]`,
  `row[2]`, `row[4]`), while `get` returns a `Subscription`.

  PASS if the reported findings include a `Repository` (or clearly
  equivalent category name) finding on `find_expiring` or on
  `expiry_notices` saying rows or storage shapes reach business code
  instead of domain objects, with SEVERITY `medium` or `low`.
  FAIL if no finding flags the rows, or if it carries SEVERITY `high`.
weight: 1
---

Reports the repository method that hands raw rows to the nightly job.
