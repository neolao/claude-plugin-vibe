---
name: expert-data-single-active-row-is-enforced-by-the-database
description: >-
  Hardening case for the uniqueness rule: an account may hold one active
  subscription, the app checks it before inserting, and a few accounts
  already hold two. A plan change cancels the current subscription and
  creates the next one. The expert must require the uniqueness in the
  database as a partial constraint over the active rows, clear the
  existing duplicates before that constraint can be created, and keep the
  cancel and the insert of a plan change in one transaction; which of two
  duplicate subscriptions survives is the only product decision left.
tags: [expert-data, recall, hardening]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
An account may have one active subscription at a time. The `subscriptions`
table (PostgreSQL, three million rows) holds every subscription ever taken:
`account_id`, `plan_id`, `started_at` and `cancelled_at`, empty while the
subscription is active. Rows are never deleted; cancelling fills
`cancelled_at`. When a customer subscribes, the signup handler first looks
for an active subscription on the account and refuses if it finds one.
Support has found a handful of accounts that currently show two active
subscriptions. We're adding plan changes: the customer picks another plan,
and their current subscription is cancelled and a new one starts on the
new plan, effective immediately.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): `REQUIREMENTS:` (non-negotiable), `RISKS:` (domain pitfalls here), `TEST SCENARIOS:` (user action → expected result). Add a fourth list, `OPEN QUESTIONS:` (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
