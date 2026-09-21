---
type: llm
focus: last_message
criteria: |
  `test_is_active_returns_false_when_missing` carries
  `@pytest.mark.skip(reason="flaky pending investigation in TICKET-501")`.
  A skipped test is `review-tests`' Dead test code check, not a
  review-hygiene concern, and the skip carries a reason and a ticket.

  PASS if review-hygiene reports no `high` or `medium` severity finding
  about this skip marker.
  FAIL if it claims the skipped test as a hygiene issue at high or medium
  severity.
weight: 1
---

Leaves the reasoned skip marker to review-tests instead of claiming it.
