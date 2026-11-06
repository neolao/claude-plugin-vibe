---
name: expert-data-renamed-column-keeps-running-code
description: >-
  Recall of the schema-compatibility bullet of expert-data: a free-text
  `users.phone` column is to become `phone_number` in a normalized format
  and required, on a two-million-row table where a third of the rows have
  no phone, while six pods are rolled out one at a time and a nightly job
  of another team reads the old column. The expert must require an
  expand/contract sequence that keeps the old column readable and
  writable until every version has moved, and a `NOT NULL` that lands
  only after a batched backfill and a decision on the rows with no value,
  instead of treating the rename and the constraint as one plain migration.
tags: [expert-data, recall, compatibility]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
The `users` table (PostgreSQL, two million rows) has a `phone` column: free
text, whatever the user typed, empty for about a third of the users. We're
replacing it with a `phone_number` column that holds the number in E.164
format (`+33612345678`), and we want it required from now on, since the new
delivery notifications need a phone number. The app runs as six pods rolled
out one at a time through the usual pipeline; a rollout takes about twenty
minutes. The nightly CRM sync, which belongs to the sales team, reads
`users.phone` directly from the database. We want this live for the start of
the delivery-notification pilot next month.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
