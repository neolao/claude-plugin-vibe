---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/orders/. `compute_discount_cents` in
  fixtures/orders/discount.py switches on `kind` (`percentage`, `fixed`,
  `bogo`); the same chain recurs in fixtures/invoicing/line_label.py and
  fixtures/admin/promo_form.py, outside the scope, and fixtures/ROADMAP.md
  announces a fourth kind (tiered).

  PASS if a finding anchored on fixtures/orders/discount.py proposes a
  Strategy registry keyed by data, a lookup table keyed by kind, or an
  equivalent named design, and names at least one of the two outside
  chains (fixtures/invoicing/line_label.py or fixtures/admin/promo_form.py)
  as evidence that the switch recurs.
  FAIL if no such design is proposed for the discount kinds, or if the
  finding cites no chain outside the scope: the in-scope switch alone is
  an isolated one, which the agent's definition says to leave alone.
weight: 2
---

Finds the recurring switch whose siblings and next variant sit outside the
path under review, and says where they are.
