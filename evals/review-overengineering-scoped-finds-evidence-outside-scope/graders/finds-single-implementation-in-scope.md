---
type: llm
focus: last_message
criteria: |
  fixtures/src/notifications/channel.py declares the abstract base class
  `NotificationChannel`; `EmailChannel`, in the same file, is its only
  implementation anywhere under fixtures/ (fixtures/src/billing/ builds
  `EmailChannel` and nothing else).

  PASS if the reported findings include a `Speculative abstraction` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/src/notifications/channel.py and that names
  `NotificationChannel` as a base class or interface with a single
  implementation.
  FAIL if no finding reports `NotificationChannel` for this reason.
weight: 2
---

Reports the one-implementation base class declared in scope: the search
for a second implementation covers the whole repository and finds none.
