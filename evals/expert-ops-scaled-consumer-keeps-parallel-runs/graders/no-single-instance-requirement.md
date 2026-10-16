---
type: llm
focus: last_message
criteria: |
  The change exists to run up to 8 replicas of the consumer at once; the
  broker hands each message to one consumer, so parallel replicas do not
  compete for the same message. The rule that a scheduled job runs one
  instance at a time is about cron-style jobs and does not apply to a
  consumer scaled on purpose.

  PASS if no REQUIREMENTS, RISKS, or TEST SCENARIOS entry requires the
  consumer to run as a single instance, caps it at one replica, wraps
  consumption in a lock or leader election, or applies a scheduler
  concurrency policy to it. Requiring that a message be processed once even
  when redelivered, that prefetch be bounded per replica, or that the
  provider's rate limit be respected across 8 replicas, is a different
  concern and passes.
  FAIL if the reply requires a single running instance, a lock or leader
  election around consumption, a concurrency policy, or treats several
  replicas consuming at once as a defect to remove.
weight: 2
---

Does not impose a single instance, a lock, or a concurrency policy on a
consumer that is being scaled out on purpose.
