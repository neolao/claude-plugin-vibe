---
name: expert-ops-poison-message-is-parked-and-alerted
description: >-
  Recall of the queue-consumer bullet of expert-ops: a consumer of a
  partner's `order.updated` messages is rewritten, and the brief recounts
  that a message the service could not parse was rejected, redelivered
  at once, and spun at the head of the queue for a weekend while nothing
  else was processed, noticed on the Monday. The expert must require, as
  requirements and not as questions, that a message still failing after
  its retries is parked with an alert instead of redelivered forever or
  dropped, and that a message is acknowledged only once its update is
  applied.
tags: [expert-ops, recall, queue-consumer]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our marketplace partner pushes an `order.updated` message onto our RabbitMQ
queue every time one of our orders changes on their side; a consumer reads
them one at a time and applies the change to the order in our database. The
partner adds fields and shapes without telling us: last spring one message
the consumer could not parse was rejected, the broker put it straight back
at the head of the queue, and the consumer rejected it again every few
milliseconds from Friday evening to Monday morning, while every message
behind it waited. We're rewriting the consumer in Go as part of the move to
the platform cluster, where it will run as one replica built by the usual
pipeline. The broker redelivers a message when the consumer that took it
dies before acknowledging it, and keeps undelivered messages for seven
days. Nobody looks at the queue unless support escalates an order.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
