---
name: expert-ops-in-scope-advice
description: expert-ops must surface config/secrets, retry/idempotency, and rolling-deploy pitfalls for a webhook worker brief
tags: [expert-ops, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this plan consultation.

Give it exactly this message:

```
Brief: we're adding a background worker that polls a new "payment-events" webhook queue
from a third-party payment provider and writes processed events into the existing
`events` Postgres table (also read by the legacy nightly reporting job). The provider
signs webhooks with a per-account secret we don't have anywhere yet, and it says
plainly in its docs that the same event can be delivered more than once. The worker
will be deployed as a second container in the same pod as the existing API service,
using the same rolling-deploy pipeline. We want it live this sprint.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Once the sub-agent returns, report its reply back verbatim.
