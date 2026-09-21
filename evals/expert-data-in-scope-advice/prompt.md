---
name: expert-data-in-scope-advice
description: expert-data must surface transaction-boundary, growing-table indexing, and deliberate delete-behavior requirements for a brief that squarely needs them
tags: [expert-data, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

We are about to plan this feature (no code exists yet):

"When a customer checks out, we deduct the purchased quantity from the `inventory` table, insert a row into the `orders` table with the total price, and call our external payment gateway to charge the customer's stored card. The `orders` table already has 5 million rows and keeps growing; the admin dashboard needs to list orders sorted by creation date, filtered by status. When an order is cancelled, we want to keep the row for accounting instead of removing it."

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief and the following request, verbatim:

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim.
