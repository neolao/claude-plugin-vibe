---
type: llm
focus: last_message
criteria: |
  The job is scheduled every 10 minutes and a backlog run has taken about 40
  minutes: without a guard, the scheduler starts a second instance while the
  first is still pushing the same paid orders, and the partner creates a
  shipment for each. Whether to guard against this is settled by the expert's
  own checklist, so it is a requirement, never a question for the Product
  Owner.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, for this job, that
  two runs must not overlap and prescribes how (the CronJob's concurrency
  policy set to forbid or replace, a lock, or an equivalent single-instance
  guard), with a stated behavior or a test scenario for the launch that
  arrives while a long run is still going (it is skipped or waits; the same
  order is not pushed twice).
  FAIL if the reply never raises overlapping runs, or raises it only as an
  `OPEN QUESTIONS:` entry asking the Product Owner whether overlap matters or
  how to handle concurrent runs.
weight: 2
---

Requires a single-instance guard for the 40-minute backlog run meeting the
next 10-minute launch, as a requirement and not an open question.
