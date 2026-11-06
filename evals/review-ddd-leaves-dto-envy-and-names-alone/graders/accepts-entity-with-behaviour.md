---
type: llm
focus: last_message
criteria: |
  `Subscription` in fixtures/subscriptions/subscription.py keeps `_status`
  and `_period_end` private, guards its own renewal and lapse in `renew`,
  and is only driven through `renew`/`cancel` by `RenewSubscription` in
  fixtures/subscriptions/renewal.py.

  PASS if no `high` or `medium` severity Anemic model, Aggregate or Entity
  finding claims `Subscription` is a data bag, that its transition is
  computed outside it, or that `RenewSubscription` holds its rules. A
  report with no findings at all passes.
  FAIL if `Subscription` or `RenewSubscription` is flagged for one of those
  reasons at high or medium severity.
weight: 1
---

Does not call an entity anemic when it owns its transitions and the use
case only orchestrates.
