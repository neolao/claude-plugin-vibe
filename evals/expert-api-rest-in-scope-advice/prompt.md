---
name: expert-api-rest-in-scope-advice
description: expert-api-rest must surface pagination, retry-safety, and backward-compatibility requirements for a brief that squarely needs them
tags: [expert-api-rest, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

We are about to plan this feature (no code exists yet):

"Partner apps integrated with our platform will get two new endpoints: one to list every comment on a blog post (some posts already have tens of thousands of comments), and one to let a partner app register a 'Like' on a post on behalf of its user. Partner apps run on flaky mobile connections, so the same Like call may be fired twice automatically when a request times out and the client retries. We also promised the partners who integrated last year that shipping this will not break anything currently working for them."

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with this brief and the following request, verbatim:

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim.
