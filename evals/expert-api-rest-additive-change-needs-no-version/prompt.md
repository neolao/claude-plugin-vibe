---
name: expert-api-rest-additive-change-needs-no-version
description: >-
  Precision side of the compatibility bullet: an existing order endpoint
  gains one optional response field and its list one optional filter, with
  partners whose clients ignore unknown fields as the API guide has always
  required. The expert must not demand a new API version, a new endpoint or
  a deprecation cycle for an additive change — it states that the change is
  additive and the existing responses stay as they are, and keeps the rest
  of its lists on the new field and filter.
tags: [expert-api-rest, precision, compatibility]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with this brief plus the consultation request below.

Brief:

```
`GET /orders/{id}` and `GET /orders` have been live for two years and three
partner integrations call them; our API guide has always required partner
clients to ignore fields they do not know, and all three were built that way.
Support agents can now attach a free-text note to an order, so we're adding an
optional `note` field to the order representation (absent when there is no
note), and an optional `?status=` filter on `GET /orders` so the admin app can
list only the cancelled orders. Nothing that exists today changes its value,
its name or its order.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
