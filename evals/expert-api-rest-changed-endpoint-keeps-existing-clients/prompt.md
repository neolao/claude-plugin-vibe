---
name: expert-api-rest-changed-endpoint-keeps-existing-clients
description: >-
  Recall of the compatibility bullet of expert-api-rest on changes that
  remove nothing: an existing order endpoint has its `shipped` status split
  into two new values and its list's default order flipped to newest first,
  while three partner integrations branch on the status value and one pages
  through the list every night. The expert must require that those clients'
  unchanged requests keep getting what they got — the old value and the old
  order, or a versioned endpoint — instead of treating a value rename and a
  default change as plain changes.
tags: [expert-api-rest, recall, compatibility]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with this brief plus the consultation request below.

Brief:

```
`GET /orders/{id}` and `GET /orders` have been live for two years. An order's
`status` is one of `new`, `paid`, `shipped`, `cancelled`. We now track the
carrier's delivery scan, so `shipped` becomes two statuses, `dispatched` and
`delivered`, and the warehouse wants `GET /orders` to list newest orders first
instead of oldest first, as it does today. Three partner integrations read
`status` to trigger their own workflows (one sends its customer an email when
it sees `shipped`), and one partner pages through `GET /orders` every night to
reconcile its books. We don't control when partners update their code.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
