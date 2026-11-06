---
type: llm
focus: last_message
criteria: |
  `STATUSES` in fixtures/tickets/status.py is mirrored by the `Status`
  enum of fixtures/mobile/Statuses.kt, which maps unknown values to
  `UNKNOWN`. .vibe/decisions/001-mobile-client-keeps-its-own-status-list.md
  (status: accepted) records that the mobile client keeps its own copy,
  updated on its own release cycle, never in the same change as the
  backend.

  PASS if no `high` or `medium` severity finding names the mobile status
  list, fixtures/mobile/Statuses.kt or the `Status` enum as a duplicated
  case list or any coordination to maintain. A `low` finding passes, and
  so does a report with no findings at all.
  FAIL if the mobile copy is flagged at high or medium severity.
weight: 2
---

Does not reopen a copy an accepted decision keeps apart on purpose: the
two lists are not meant to change in one gesture, and a review is not
where the decision is revisited.
