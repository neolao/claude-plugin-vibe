---
type: tool_used
tool: Agent
input_match: "vibe:review-(tests|naming|security|dependencies|robustness|hygiene|antipatterns|simplicity|overengineering|correctness|comments|signatures|coordination)"
min: 13
max: 26
weight: 2
---

CLAUDE.md here has no `## Review agents` table, so Step 1 must fall back to the
skill's own default list: the thirteen always-active agents (tests, naming,
security, dependencies, robustness, hygiene, antipatterns, simplicity,
overengineering, correctness, comments, signatures, coordination), each
launched once. `min: 13` asserts none was skipped; `max: 26` leaves room for a
rare retry without letting the count silently include a conditional agent
(those are checked separately, at zero, below).
