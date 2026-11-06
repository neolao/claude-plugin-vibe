---
type: llm
focus: last_message
criteria: |
  `RenewalService.renew` in fixtures/subscriptions/renewal.py reads
  `sub.status`, `sub.period_end` and `sub.plan`, decides whether the
  subscription lapses or gets a new period end, and writes `sub.status` and
  `sub.period_end` back through the public attributes of `Subscription`
  (fixtures/subscriptions/subscription.py), which has no method of its own.

  PASS if the reported findings include an `Anemic model` (or clearly
  equivalent category name, e.g. "Aggregate" or "Entity") finding anchored
  on fixtures/subscriptions/renewal.py or fixtures/subscriptions/subscription.py
  whose ISSUE or SUGGESTION names the renewal / lapse logic of `renew` as
  what should move onto `Subscription` (a `renew` or similar method
  guarding the transition), with SEVERITY `medium` or `low`.
  FAIL if no finding flags this logic sitting in the service, or if the
  only finding on it merely asks for getters, or if it carries SEVERITY
  `high`.
weight: 2
---

Reports the service that computes the subscription's own transition and
period from its fields and writes them back, naming the logic to migrate.
