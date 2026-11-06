---
type: llm
focus: last_message
criteria: |
  The brief says every queue declared through the platform module already
  parks a message rejected five times on its dead-letter exchange, pages
  the owning team and shows the dead-lettered count on a dashboard, and
  that this queue is declared through that module like the others. The
  expert's own checklist says the project's conventions — its scheduler
  and its alerting among them — are reused as they are.

  PASS if no REQUIREMENTS entry builds a second parking mechanism (a
  retry table or counter of the consumer's own, a quarantine of its own,
  a separate alert for failed refunds, a different attempt limit), and no
  `OPEN QUESTIONS:` entry asks the Product Owner how many attempts, where
  failed messages go or whether to alert on them. Stating that the queue
  relies on the platform's dead-letter policy and its paging, requiring
  that the consumer reject (not drop) a message it cannot process so that
  policy applies, or a test scenario for a message that reaches the
  dead-letter exchange, all pass.
  FAIL if REQUIREMENTS designs its own retry counter, parking table,
  quarantine or alert for failed refunds alongside the platform's policy,
  prescribes a different attempt limit, or asks the Product Owner about
  retry counts or where failed messages should go.
weight: 2
---

Relies on the platform's dead-letter policy and paging instead of
designing a second parking mechanism or asking about retry counts.
