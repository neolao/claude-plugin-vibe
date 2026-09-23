---
name: expert-ui-ux-out-of-scope-redirect
description: expert-ui-ux must decline/redirect a pure visual-restyling brief instead of inventing flow/state advice
tags: [expert-ui-ux, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ui-ux` sub-agent (Agent tool, `subagent_type: "vibe:expert-ui-ux"`) with this plan consultation.

Give it exactly this message:

```
Brief: we're refreshing the visual style of the marketing site header: switch the color palette over to the new brand tokens, apply the new type scale to the nav links and logo lockup, tighten the spacing to the 8px grid, and add a dark mode variant built from the existing dark tokens. Nothing about the header's links, structure, or behavior changes.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
