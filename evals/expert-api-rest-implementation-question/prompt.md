---
name: expert-api-rest-implementation-question
description: >-
  The experts' second consultation format, used by workflow.md during
  implementation rather than at plan time: one precise question with minimal
  code context must come back as one concrete justified recommendation plus
  the rejected alternative, in a few sentences — not the three-list plan
  format and not a checklist.
tags: [expert-api-rest, implementation-consultation, format]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

We are mid-implementation on an approved plan. The plan says the cancellation endpoint returns the cancelled order; it does not say what to do when the order is already cancelled, and neither the codebase nor the plan answers it.

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with exactly this question and request:

```
`POST /orders/{id}/cancel` returns `200` with the cancelled order. A client that retries the call on an order it already cancelled currently gets the same `200` with the same body. The endpoint has no other side effect on an already-cancelled order.

Give me one concrete justified recommendation plus the rejected alternative, in a few sentences.
```

Report the sub-agent's reply back verbatim.
