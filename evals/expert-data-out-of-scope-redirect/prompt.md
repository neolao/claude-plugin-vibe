---
name: expert-data-out-of-scope-redirect
description: expert-data must decline/redirect a pure HTTP-status-code brief instead of inventing API advice
tags: [expert-data, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

We are about to plan this feature (no code exists yet — this is purely about the HTTP contract, nothing about the data model or storage):

"We're deciding what HTTP status code our existing 'cancel order' endpoint should return. Should a successful cancellation return 200 or 204? And if the client calls it again on an order that is already cancelled, should that retry return 409 Conflict or just 200 again?"

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief and the following request, verbatim:

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim.
