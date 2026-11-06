---
name: expert-data-processed-marker-keeps-to-the-schema
description: >-
  Recall side of the operations routing: a nightly export job gets a
  `processed_at` column on a twenty-million-row table so that a rerun
  skips the rows already sent, and the brief says the job's schedule,
  single-instance guarantee, timeout and alerting are written alongside
  by the platform team. The column and its query are expert-data's
  domain: it must fill its lists with the index the unmarked-rows query
  needs and what the first run does with the existing rows — and leave
  the concurrency policy, the timeout and the alert out of its
  REQUIREMENTS, since the scope sentence routes those to `expert-ops`.
tags: [expert-data, recall, ops-routing]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
Every night a job reads the `events` table (PostgreSQL, twenty million rows,
about fifty thousand added per day for two years) and sends the new events
to the accounting tool. Today it relies on "events created since yesterday",
so a run that crashes half-way sends some events twice the next night and
never sends the ones it skipped. We're adding a `processed_at` column on
`events`: the job selects the rows where it is empty, oldest first, sends
them in batches and marks each batch as it goes, so a rerun carries on where
the previous run stopped. The platform team is writing the job's schedule,
its one-instance-at-a-time guarantee, its timeout and the alert on failure
alongside this change.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
