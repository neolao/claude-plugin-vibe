---
name: expert-api-rest-out-of-scope-redirect
description: expert-api-rest must decline/redirect a pure database-schema brief instead of inventing REST advice
tags: [expert-api-rest, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

We are about to plan this feature (no code exists yet — this is purely about the database, nothing about an API):

"We're adding a `discount_reason` column to the existing `orders` table so support agents can record why a manual discount was applied. We need to decide the column type, whether it should be nullable, and whether it needs an index for the reporting queries that filter orders by discount reason."

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with this brief and the following request, verbatim:

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim.
