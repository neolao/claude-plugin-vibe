---
name: expert-frontend-design-asks-real-product-decision
description: >-
  Precision side of the open-questions rule: on a customer-branding brief,
  expert-frontend-design must still put the one genuine product decision
  (whether the product's own branding stays visible next to the customer's)
  to the Product Owner, while settling the pickable design details itself —
  the contrast of an arbitrary brand color, the logo constraints, dark mode,
  the header at narrow widths.
tags: [expert-frontend-design, precision, open-questions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-frontend-design` sub-agent (Agent tool, `subagent_type: "vibe:expert-frontend-design"`). Give it exactly this prompt:

```
We're adding customer branding to the client portal. Each customer can upload their logo and pick one brand color, and the portal their own users log into should then look like the customer's product. The portal is built on our design system (color, type and spacing tokens, a component library, a light and a dark theme). Today our own logo sits top-left in the navigation bar and our company name in the footer of every page.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
