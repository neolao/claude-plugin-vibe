---
name: expert-ops-bus-consumer-keeps-to-the-operation
description: >-
  Recall side of the routing by id: a new consumer reads `invoice.issued`
  from the platform's bus and writes one row per invoice into a new
  archive table, whose columns, constraints and indexes the data team is
  designing alongside. The consumer's operation is expert-ops's domain:
  it must fill its lists with the consumer's credentials, its shutdown
  with a message in flight, the timeout on the write, a redelivered
  message writing no second row, and the alert when it stops — and leave
  the column types, the constraints and the index out of its
  REQUIREMENTS, since the scope sentence routes the schema to
  `expert-data`.
tags: [expert-ops, recall, routing]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Accounting needs every invoice kept for ten years even after the customer
closes their account. We're adding a consumer that reads the
`invoice.issued` messages the billing service publishes on the platform's
RabbitMQ and writes one row per invoice into a new `invoice_archive` table
in the reporting database; the data team is designing the table's columns,
constraints and indexes alongside this change. The broker redelivers a
message when the consumer that took it dies before acknowledging it, and
keeps undelivered messages for seven days. The consumer will run as one
replica in the platform cluster, built by the usual pipeline, with
credentials for the bus and for the reporting database that no service
holds today. Nobody looks at it once it is live.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
