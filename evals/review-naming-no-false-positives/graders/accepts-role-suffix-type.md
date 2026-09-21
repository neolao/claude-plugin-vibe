---
type: llm
focus: last_message
criteria: |
  `OrderRepository` names a recognised architectural role, not one of the
  vague `Manager`/`Helper`/`Utils` suffixes the checklist targets.

  PASS if no `high` or `medium` severity Type finding calls this name vague,
  generic, or hiding a second responsibility.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a role-named type vaguely suffixed.
