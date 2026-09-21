---
type: tool_used
tool: Agent
input_match: "vibe:review-(tests|naming|security|dependencies|robustness|hygiene|antipatterns|simplicity|overengineering)"
min: 9
max: 20
weight: 2
---

CLAUDE.md here has no `## Review agents` table, so Step 1 must fall back to the
skill's own default list: review-tests, review-naming, review-security,
review-dependencies, review-robustness, review-hygiene, review-antipatterns,
review-simplicity, and review-overengineering are always active — exactly 9
agents, each expected to be launched once. `min: 9` asserts none of the
always-active set was skipped; `max: 20` leaves room for a rare retry without
letting the count silently include a conditional agent (those are checked
separately, at zero, below).
