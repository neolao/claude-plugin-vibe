---
name: expert-data-scheduled-job-brief-names-expert-ops
description: >-
  Precision side of the operations routing: an existing nightly cleanup
  job, whose SQL and tables do not change, is moved under the platform's
  scheduler with a single-instance guarantee, a timeout, structured logs
  and an alert when it fails or never starts — a brief full of database
  vocabulary that changes no schema, migration, query or transaction.
  expert-data must decline in one line and name `expert-ops` by id, since
  the experts never see the roster, instead of filling the lists with
  scheduling advice or re-deriving batching rules for a query that does
  not change.
tags: [expert-data, precision, ops-routing]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
Our nightly cleanup job deletes the `sessions` rows older than ninety days.
It has run for two years from a developer's crontab on one of the app
servers, in batches of ten thousand rows; its SQL, the table it touches and
the rows it deletes do not change. We're moving it under the platform's
scheduler (a Kubernetes CronJob): it must never run twice at the same time,
be safe to start again after a crash mid-way, stop after an hour if it is
still running, write structured logs with a run id, and page the on-call
engineer when a run fails or does not start at all. Nothing in the schema,
the queries or the application changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
