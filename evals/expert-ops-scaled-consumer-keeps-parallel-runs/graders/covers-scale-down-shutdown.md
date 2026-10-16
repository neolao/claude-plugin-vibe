---
type: llm
focus: last_message
criteria: |
  Scaling back down to one replica, like a rolling deploy, stops replicas
  that are in the middle of a message: the platform sends SIGTERM and kills
  the process after a grace period. The expert's own checklist requires
  graceful shutdown on SIGTERM, so this is settled.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, for this consumer,
  what a replica does when it is stopped by scale-down or a deploy with a
  message in flight: it stops taking new messages and finishes and
  acknowledges the current one within the grace period, or hands it back to
  the broker unacknowledged, so the email is neither lost nor left in limbo —
  with a test scenario or a stated behavior for a replica stopped mid-message.
  FAIL if the reply never addresses a replica being stopped while handling a
  message, or treats scale-down as free of consequences for in-flight work.
weight: 2
---

Requires a replica stopped by scale-down or a deploy to finish or hand back
its in-flight message, as the graceful-shutdown rule in the checklist
requires.
