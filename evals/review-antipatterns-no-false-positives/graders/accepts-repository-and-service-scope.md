---
type: llm
focus: last_message
criteria: |
  `OrderRepository` persists and retrieves orders — reading the order's own
  fields to build the row it writes is the job it exists for — and
  `OrderService.place_order` charges then saves through two injected
  collaborators.

  PASS if no `high` or `medium` severity God object or Feature envy finding
  targets either class.
  FAIL if either is flagged at high or medium severity.
weight: 1
---

Does not call a repository's own persistence work feature envy or a god object.
