---
type: llm
focus: last_message
criteria: |
  The API has dashboards, alerts, and health and readiness probes; a CronJob
  has none of those. If the partner API is down for a night, the credentials
  stop working, or the job is never scheduled, nothing goes red: paid orders
  stop shipping and the gap is found when finance reconciles, up to a week
  later.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS requires that a failed run
  or a run that never happened is noticed without someone reading logs: the
  job exits non-zero on failure and an alert fires on failed or missed runs
  (a last-successful-run or unshipped-paid-orders metric with a threshold, an
  alert on the CronJob's failed-job count, a dead man's switch, or an
  equivalent), with a test scenario or a stated behavior for a run that
  fails.
  FAIL if the only observability the reply asks for is logging (structured or
  not), if it relies on health or readiness probes the job does not have, or
  if a failed or missed run reaching nobody is never raised.
weight: 2
---

Requires a failed or never-started run to be alerted on, since the job has
no health endpoint and nobody watches it until finance reconciles.
