---
type: llm
focus: last_message
criteria: |
  The brief says the job's schedule, its single-instance guarantee, its
  timeout and its alerting are written alongside by the platform team. The
  expert's scope sentence keeps the column, the index and the batching
  here and routes how a scheduled job is run, deployed, observed and kept
  running to `expert-ops`.

  PASS if no REQUIREMENTS entry prescribes the scheduler's concurrency
  policy, the lock, the timeout value, the log fields or the alert.
  Mentioning them in passing as another expert's domain, naming
  `expert-ops`, or requiring that a run which stops mid-way leaves the
  rows it did not finish unmarked (so the next run picks them up), all
  pass: what a rerun reads from the table is the schema's.
  FAIL if REQUIREMENTS prescribes how the CronJob prevents overlapping
  runs, which timeout it gets, what its logs carry or how its failure is
  alerted on, as if the expert owned the job's operation.
weight: 1
---

Keeps the concurrency policy, the timeout, the logs and the alert out of
its REQUIREMENTS: the marker column and its query are its domain, the
job's operation is `expert-ops`'s.
