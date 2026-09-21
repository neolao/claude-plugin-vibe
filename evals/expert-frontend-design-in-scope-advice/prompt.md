---
name: expert-frontend-design-in-scope-advice
description: expert-frontend-design must surface token/dark-mode reuse, responsive stacking, and semantic-color contrast for a pricing page brief
tags: [expert-frontend-design, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-frontend-design` sub-agent (Agent tool, `subagent_type: "vibe:expert-frontend-design"`). Give it exactly this prompt:

```
We're adding a new pricing page. It shows a comparison table with three tiers side by side — Starter, Pro, and Enterprise — and Pro is the tier we want most customers to pick, so it needs to stand out as the "Recommended" option among the three. The app already has a design system (spacing/type tokens, a component library, and a light + dark theme) — reuse it rather than one-off styling. On phones, the three-column comparison table can't stay three columns wide; it needs to still be usable there.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Once the sub-agent returns, report its findings back verbatim.
