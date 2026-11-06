---
name: expert-data-convention-does-not-excuse-missing-foreign-key
description: >-
  Precision side of the convention rule: the schema's eleven existing
  tables have no foreign keys and store amounts as `double precision`,
  and the brief adds an invoices table whose totals an accounting export
  sums. "Reuse the existing conventions" must not become "copy the
  existing defect": expert-data must still require an exact amount type
  and a database-enforced foreign key to customers on the new table, and
  must not make adding foreign keys to the eleven existing tables — which
  hold orphaned rows — a requirement of this change.
tags: [expert-data, precision, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
Our PostgreSQL schema has eleven tables, all with an integer `id`, snake_case
names and `created_at`/`updated_at` columns. None of them has a foreign key:
the app checks that a referenced row exists before writing, and we know a
few `orders` rows point at customers that were deleted years ago. Amounts
(`orders.total`, `payments.amount`) are `double precision`. We're adding an
`invoices` table: the customer it is for, the invoice number, the total
amount and the date issued. The monthly accounting export sums the invoice
totals per customer and the figures go to the auditors. Nothing else in the
schema changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
