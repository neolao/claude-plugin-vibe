---
name: expert-data-frozen-snapshot-does-not-follow-its-source
description: >-
  Precision side of the derived-value bullet: an invoice-lines table
  copies the product's name and unit price at the moment the invoice is
  issued, so that the invoice keeps saying what the customer was charged
  after the product is renamed, repriced or removed. The expert must not
  demand a trigger, a rebuild or a cascading update that keeps the copy
  in step with the products table, nor replace the copy with a join —
  the snapshot is frozen on purpose — and keeps its lists on the line's
  exact amount type and its immutability once issued.
tags: [expert-data, precision, derived-data]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
We're adding invoicing. An `invoices` table (the customer, the number, the
date issued) and an `invoice_lines` table: the product, the quantity, and
the product's name and unit price as they were when the invoice was issued.
Products get renamed and repriced all the time and are sometimes removed
from the catalogue, and an invoice must keep showing exactly what the
customer was charged, as the auditors compare it with the PDF the customer
received. The `products` table already exists and does not change.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
