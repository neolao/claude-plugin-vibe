---
name: expert-ops-schema-brief-names-expert-data
description: >-
  Precision side of the routing by id: a `NOT NULL` column with a default
  and a batched backfill on a large table, applied by the project's
  migration tool through the pipeline's existing migrate stage as every
  migration before it — a brief full of deployment vocabulary (pods,
  rollout, backfill) that changes nothing in how the service is
  configured, deployed, observed or kept running. expert-ops must decline
  in one line and name `expert-data` by id, since the experts never see the
  roster, instead of filling the lists with rollout advice for a
  migration whose run does not change.
tags: [expert-ops, precision, routing]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
We're adding a `country` column to the `addresses` table (PostgreSQL, eight
million rows) so that shipping rates can be computed per country: a
two-letter code, `NOT NULL`, defaulting to the account's country, with the
existing rows backfilled in batches from the account before the constraint
is added. The migration is written with the project's migration tool and
runs the way every migration has for three years: the pipeline's `migrate`
stage applies it before the pods roll, and a failed migration stops the
deploy. Nothing changes in how the service is configured, built, deployed,
logged or alerted on, and no job or consumer is added.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
