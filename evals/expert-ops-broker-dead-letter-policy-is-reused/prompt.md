---
name: expert-ops-broker-dead-letter-policy-is-reused
description: >-
  Precision side of the queue-consumer bullet: the platform's broker
  already parks a message rejected five times on a dead-letter exchange
  that pages the owning team, with a dashboard per queue. A consumer that
  requests refunds from the payment provider is added. The expert must not
  design a second parking mechanism, a retry counter or an alert of its
  own, nor ask the Product Owner about retry counts — the platform's
  policy is the convention — while still requiring that a redelivered
  message refunds no customer twice and that the message is acknowledged
  only after the provider has accepted the refund.
tags: [expert-ops, precision, queue-consumer]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Every queue on the platform's RabbitMQ is declared through the platform
team's module, which attaches the same policy to all of them: a message
rejected five times goes to the queue's dead-letter exchange, the platform's
alert pages the team that owns the queue, and each queue has a dashboard
showing its depth, its oldest message and its dead-lettered count. We're
adding a consumer for `refund.requested` messages that calls the payment
provider's refund API, one message at a time, then marks the order as
refunded; the provider accepts a client reference on each refund call. The
broker redelivers a message when the consumer that took it dies before
acknowledging it. The consumer runs as one replica in the platform cluster,
built by the usual pipeline; the queue is declared through the platform
module like the others.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
