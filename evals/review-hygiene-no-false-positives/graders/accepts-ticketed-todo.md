---
type: llm
focus: last_message
criteria: |
  The comment above `calculate_discounted_total` in
  fixtures/order_repository.py is `# TODO(JIRA-4231): revisit rounding once
  finance confirms the new promo rules` — a TODO carrying a ticket
  reference.

  PASS if no `high` or `medium` severity finding calls this marker stale,
  untracked, or orphaned.
  FAIL if it is flagged as a Stale marker (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a ticket-referencing TODO a stale marker.
