---
name: expert-ui-ux-in-scope-advice
description: expert-ui-ux must surface partial-success state, inline recoverable errors, and flow-interruption handling for a CSV bulk-import brief
tags: [expert-ui-ux, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ui-ux` sub-agent (Agent tool, `subagent_type: "vibe:expert-ui-ux"`). Give it exactly this prompt:

```
We're adding a CSV bulk-import feature so admins can create many user accounts at once. An admin uploads a CSV, the app checks every row, and creates the accounts for the rows that pass. Some rows will fail — a bad email format, a duplicate username, a missing required field. The CSV can be large, so checking it takes a few seconds.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Once the sub-agent returns, report its findings back verbatim.
