---
name: expert-api-rest-new-endpoint-follows-existing-conventions
description: >-
  Recall of the convention rule of expert-api-rest: a three-year-old public
  API already paginates with page numbers, writes camelCase, wraps errors in
  its own envelope and nests resources under the account, and partners
  generated their clients from it. Two endpoints are added. The expert must
  require that they reuse those conventions as they are — not prescribe
  cursor pagination, snake_case, a problem-details envelope or a flatter
  URL for the new endpoints — and still require the new list to be
  paginated.
tags: [expert-api-rest, recall, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with this brief plus the consultation request below.

Brief:

```
Our public API has had fourteen endpoints for three years and partners
generated their clients from its OpenAPI file. Every endpoint nests under the
account, like `/accounts/{accountId}/projects/{projectId}/tasks/{taskId}`;
JSON fields are camelCase; every list takes `?page=` and `?pageSize=` and
returns the items under `data` with a `meta.totalCount`; every error is
`{ "error": { "code": "...", "message": "..." } }`. We're adding comments on
tasks: one endpoint to list the comments of a task (a few tasks have thousands)
and one to post a comment. Nothing else in the API changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
