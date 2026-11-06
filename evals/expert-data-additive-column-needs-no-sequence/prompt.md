---
name: expert-data-additive-column-needs-no-sequence
description: >-
  Precision side of the schema-compatibility bullet: a two-million-row
  `users` table gains one optional `timezone` column and a new
  `user_preferences` table, with every existing column left exactly as it
  is, while six pods roll out one at a time and another team's nightly
  job reads the table. The expert must not demand a dual-write period, a
  transitional column, a multi-release sequence or a backfill for an
  additive change — it states that the running version ignores what was
  added, and keeps the rest of its lists on the new column and the new
  table.
tags: [expert-data, precision, compatibility]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
The `users` table (PostgreSQL, two million rows) is read and written by the
app, which runs as six pods rolled out one at a time, and read directly by
the sales team's nightly CRM sync. We're letting users pick their time zone
so that delivery notifications show local times: a `timezone` column on
`users`, empty until the user picks one (the app then falls back to the
account's country), and a new `user_preferences` table holding the
notification settings a user can turn on or off. Nothing that exists
changes: every current column keeps its name, type and meaning, and the
CRM sync keeps reading what it reads today.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
