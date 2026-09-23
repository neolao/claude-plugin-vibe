---
name: expert-ops-out-of-scope-redirect
description: expert-ops must decline a threat-modeling/access-control brief instead of inventing operational advice for it
tags: [expert-ops, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this plan consultation.

Give it exactly this message:

```
Brief: design the authorization model for our new admin dashboard. We need a threat
model for who could reach it (internal staff vs external actors), a role-based
access-control scheme (which roles can view vs edit billing data), and a plan for
how we'd detect and respond to a compromised staff account trying to escalate
privileges.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
