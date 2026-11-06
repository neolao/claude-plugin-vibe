---
name: expert-api-rest-convention-does-not-excuse-unbounded-list
description: >-
  Precision side of the convention rule: the API's six existing list
  endpoints return their whole collection with no pagination, and the brief
  adds a list of audit events that grows by millions a year. "Reuse the
  existing conventions" must not become "copy the existing defect":
  expert-api-rest must still require the new list to be paginated, and must
  not make re-paginating the six existing lists — a breaking change for
  their clients — a requirement of this change.
tags: [expert-api-rest, precision, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with this brief plus the consultation request below.

Brief:

```
Our internal API has six list endpoints (`/users`, `/teams`, `/roles`, and three
others) and each one returns its whole collection as a JSON array; the largest
holds about two hundred items, and the five apps that call them, written by
other teams, read the arrays directly. Fields are camelCase and errors come
back as `{ "error": { "code": "...", "message": "..." } }`. We're adding an
endpoint that lists the audit events of the account (who changed what, when):
the table already holds four million rows and grows by about a million a year.
The admin app will show them newest first and filter them by user and by date.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
