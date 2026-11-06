---
name: expert-ops-sandbox-default-is-required-in-production
description: >-
  Recall of the default rule in expert-ops's config bullet: a refund
  worker reads the payment provider's base URL from a new variable that
  the brief wants defaulting to the provider's sandbox so that the worker
  starts on a laptop with nothing set, and the production deploy is
  expected to set the live URL. A production pod with the variable
  missing would send real refunds to the sandbox and report success. The
  expert must require that this value has no production-unsafe default —
  required, failing fast at startup when missing — as a requirement, not
  a question.
tags: [expert-ops, recall, config-defaults]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
We're adding a worker to our Node service that processes the refunds
support agents approve during the day: it reads each approved refund and
calls the payment provider's refund API, then marks the order as refunded
and emails the customer. The service reads its configuration from
environment variables through the existing `config` module, which gives
each variable a default. The provider has a sandbox (`sandbox.pay.example`)
and a live API (`api.pay.example`), with different keys; we'd like the
worker's `PAYMENT_API_URL` to default to the sandbox so that it runs on a
developer's laptop with nothing set, and the production deploy will set the
live URL and key. The worker runs as one replica from the same image as the
API, through the usual pipeline. Finance reconciles refunds against the
provider's statement once a month.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
