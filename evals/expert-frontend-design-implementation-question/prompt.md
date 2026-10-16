---
name: expert-frontend-design-implementation-question
description: >-
  The experts' second consultation format, used by workflow.md during
  implementation rather than at plan time: one precise question about a
  design detail the expert can decide itself must come back as one concrete
  justified recommendation plus the rejected alternative, in a few sentences —
  not the three-list plan format, not a checklist, and never handed back to
  the Product Owner as a choice to make.
tags: [expert-frontend-design, implementation-consultation, format]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

We are mid-implementation on an approved plan. The plan requires the pricing page's tier comparison table to stay usable on phones; it does not say how, and neither the codebase nor the plan-time brief answers it.

Invoke the `vibe:expert-frontend-design` sub-agent (Agent tool, `subagent_type: "vibe:expert-frontend-design"`) with exactly this question and request:

```
The pricing page compares three tiers (Starter, Pro, Enterprise) over about twelve feature rows, built with the design system's `Table` component, which has no responsive mode: below 480px it overflows the page horizontally. The design system also ships a `Card` component and a `ScrollArea` component (horizontal scrolling with edge fades). Which narrow-width treatment should the comparison table get?

Give me one concrete justified recommendation plus the rejected alternative, in a few sentences.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
