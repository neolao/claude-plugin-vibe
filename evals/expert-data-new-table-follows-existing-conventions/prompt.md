---
name: expert-data-new-table-follows-existing-conventions
description: >-
  Recall of the convention rule of expert-data: a six-year-old schema
  already uses integer ids, snake_case plural names, `timestamptz` audit
  columns, an `archived_at` column instead of deletes and numbered SQL
  files run by Flyway, and a reporting team queries it directly. A table
  is added. The expert must require that it reuses those conventions as
  they are — not prescribe a UUID key, a `deleted` flag, a different
  naming or an ORM migration for the new table — and still require the
  foreign key and the index for its listing query.
tags: [expert-data, recall, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
Our PostgreSQL schema has had forty tables for six years. Every table has a
`bigserial` integer `id`, a snake_case plural name (`tasks`, `task_labels`),
`created_at` and `updated_at` columns as `timestamptz`, and a nullable
`archived_at` column: we never delete rows, we set `archived_at`, and every
list query filters on `archived_at IS NULL`. Migrations are numbered SQL
files (`V0412__add_task_labels.sql`) run by Flyway in the deploy pipeline.
The reporting team queries the database directly with its own SQL. We're
adding comments on tasks: a `comments` table with the author, the task, the
text and when it was posted; the app lists the comments of one task, oldest
first, and a few tasks have thousands. Nothing else in the schema changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
