---
type: llm
focus: last_message
criteria: |
  The script is scheduled every 10 minutes and one run can take over an
  hour: without a guard, cron starts a second instance while the first is
  still loading and archiving the same files. Whether to guard against this
  is settled by the expert's own checklist, so it is a requirement, never a
  question for the Product Owner.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, for this script,
  that two runs must not overlap and prescribes a single-instance guard
  (`flock`, a lock file with a stale-lock strategy, or an equivalent), with
  a test scenario or a stated behavior for the second launch (it exits or
  skips, it does not process the same files twice).
  FAIL if the reply never raises overlapping runs, or raises it only as an
  `OPEN QUESTIONS:` entry asking the Product Owner whether a lock is wanted
  or how to handle concurrent runs.
weight: 2
---

Requires a single-instance guard for the hour-long run meeting the next
ten-minute launch, as a requirement and not an open question.
