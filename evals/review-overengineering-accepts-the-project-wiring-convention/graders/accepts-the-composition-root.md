---
type: llm
focus: last_message
criteria: |
  fixtures/src/app.py is the composition root: `build_app` builds every
  service (`PostgresOrderRepository`, `SmtpSender`, `InvoiceRenderer`,
  `InvoiceMailer`, `PlaceOrder`) and hands each its dependencies through
  its constructor; fixtures/CLAUDE.md says every service is wired there.

  PASS if no `high` or `medium` severity finding (Pattern without need,
  Speculative abstraction, Disproportionate structure or any other
  category) targets fixtures/src/app.py, `build_app` or the `App`
  class. A `low` finding passes, and so does a report with no findings
  at all.
  FAIL if the composition root is reported as DI scaffolding, ceremony or
  an unneeded layer at high or medium severity.
weight: 2
---

Does not call the composition root ceremony: wiring every service in
one place is the project's convention, not a pattern without need.
