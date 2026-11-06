---
type: llm
focus: last_message
criteria: |
  The change makes the batch size and the timeout adjustable at runtime
  so an on-call engineer can lower them during an incident, on a job that
  runs unattended every night and whose accounting-tool calls now time
  out on large batches.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS covers at least one of:
  a batch that still times out at the configured size is retried only if
  the accounting tool accepts the same batch twice without duplicating the
  orders (or the run stops and is alerted on, rather than silently
  skipping the batch); a lowered batch size making the run longer than the
  CronJob's interval, and what the concurrency policy or lock does then;
  the value an engineer sets during an incident being visible in the run's
  logs so the next run's behaviour can be explained.
  FAIL if the lists never go beyond "make the two values configurable"
  and say nothing about a batch that still fails, a run that outlasts the
  interval, or where the effective values can be seen.
weight: 1
---

Spends the lists on what the tunables change — a batch that still times
out, a longer run, the values an engineer set — instead of on making them
required.
