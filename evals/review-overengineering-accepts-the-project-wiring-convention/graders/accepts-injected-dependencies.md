---
type: llm
focus: last_message
criteria: |
  `InvoiceMailer` in fixtures/src/invoicing/mailer.py receives its
  `renderer` and `sender` through its constructor; fixtures/src/app.py
  builds it with `InvoiceRenderer()` and `SmtpSender(smtp_host)`, and
  fixtures/tests/test_mailer.py builds it with a `RecordingSender` to
  assert on what was sent. Every service in the project is wired the
  same way.

  PASS if no `high` or `medium` severity finding (Pattern without need,
  Speculative abstraction or any other category) targets `InvoiceMailer`,
  its constructor parameters, `SmtpSender` or `InvoiceRenderer` for
  being injected rather than constructed directly. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if `InvoiceMailer` receiving its collaborators through its
  constructor is reported as DI scaffolding or an unneeded seam at high
  or medium severity.
weight: 2
---

Does not ask for a direct call where the project injects everything:
one more injected dependency follows the convention review-solid's D
would otherwise enforce.
