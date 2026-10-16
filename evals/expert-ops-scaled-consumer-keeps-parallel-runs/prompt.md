---
name: expert-ops-scaled-consumer-keeps-parallel-runs
description: >-
  Precision side of the scheduled-job rule: a queue consumer being autoscaled
  from 1 to 8 replicas is not a scheduled job — running several instances at
  once is the point of the change. expert-ops must not require a single
  instance, a lock, or a concurrency policy on it, while still requiring what
  its checklist settles for a scaled consumer: a replica stopped by
  scale-down or a deploy finishes or hands back its in-flight message, and a
  redelivered message does not send the email twice.
tags: [expert-ops, precision, scheduled-job]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our order-confirmation emails are sent by a consumer service that reads the
`order.paid` messages from RabbitMQ and calls the email provider's API, one
message at a time, from a single replica. During sales the queue backs up for
hours. We're changing its deployment so it autoscales from 1 to 8 replicas on
queue depth and scales back down when the queue is drained. The broker
redelivers a message when the consumer that took it dies before acknowledging
it. The consumer runs in the same cluster and goes through the same image
pipeline as the rest of the platform.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
