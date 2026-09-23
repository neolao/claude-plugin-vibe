---
name: expert-frontend-design-out-of-scope-redirect
description: expert-frontend-design must decline/redirect a pure flow-and-state checkout brief instead of inventing visual-design advice
tags: [expert-frontend-design, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-frontend-design` sub-agent (Agent tool, `subagent_type: "vibe:expert-frontend-design"`). Give it exactly this prompt:

```
No code exists yet — this is purely about the checkout's step logic and saved progress, nothing about how the screens look. We're reworking the multi-step checkout flow: step 1 cart review, step 2 shipping address, step 3 payment, step 4 confirmation. The customer must be able to go back to a previous step without losing what they already entered, and if they close the tab mid-checkout and return later, their progress must still be there. Also define what happens across the steps if the payment step fails.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
