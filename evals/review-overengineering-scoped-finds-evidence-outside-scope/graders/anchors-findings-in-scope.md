---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/src/notifications/. Files
  outside it (fixtures/src/billing/invoices.py,
  fixtures/src/billing/reminders.py, fixtures/src/billing/money.py,
  fixtures/src/billing/pricing.py) may be named inside a finding's ISSUE
  or SUGGESTION as evidence. fixtures/src/billing/pricing.py declares a
  `PricingStrategy` base class that `StandardPricing` alone implements,
  and fixtures/src/billing/money.py declares `format_money(amount,
  currency)` whose every caller — fixtures/src/notifications/digest.py
  included — passes `currency="EUR"`: both are declared outside the
  scope.

  PASS if every finding's FILE: line points to a file under
  fixtures/src/notifications/, and no finding reports `PricingStrategy`,
  `StandardPricing`, `format_money` or its `currency` parameter —
  whatever its FILE: line. A sentence outside any finding block saying
  that one of them exists but is out of scope passes.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/src/notifications/, or if any finding (a FILE: block) reports
  `PricingStrategy` or the `currency` parameter of `format_money`, even
  one anchored on fixtures/src/notifications/digest.py.
weight: 2
---

Keeps every finding anchored on a file in scope and leaves machinery
declared outside the scope alone, even where its use is in scope: the
whole repository is read for evidence, and the full review owns the
rest.
