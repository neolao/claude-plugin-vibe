---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/src/notifications/.
  fixtures/src/billing/money.py, outside the scope, declares
  `format_money(amount, currency)`; every caller passes `currency="EUR"`,
  including fixtures/src/notifications/digest.py, which is in scope.

  PASS if no finding reports `format_money` or its `currency` parameter —
  whatever its severity and wherever its FILE: line points, including a
  finding anchored on fixtures/src/notifications/digest.py. A report with
  no findings at all passes, and so does a sentence outside any finding
  block saying the parameter never varies but is declared out of scope.
  FAIL if any finding (a FILE: block) reports `format_money` or its
  `currency` parameter.
weight: 2
---

Reports nothing on a parameter declared outside the scope, even though
one of the call sites passing the same value is in scope: the finding
belongs where the parameter is declared, and that file is the full
review's.
