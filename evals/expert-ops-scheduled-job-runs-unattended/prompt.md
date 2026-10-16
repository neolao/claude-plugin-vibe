---
name: expert-ops-scheduled-job-runs-unattended
description: >-
  A job is moving from a request handler to a platform-scheduled run with no
  health endpoint and nobody watching it: expert-ops must require what the
  scheduled shape changes — one instance at a time when a backlog run outlasts
  the interval, a rerun after a crash mid-batch that creates no second
  shipment, and a failed or never-started run that is alerted on instead of
  only logged — as requirements, not as questions to the Product Owner.
tags: [expert-ops, recall, scheduled-job]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
We're adding a job to our Node service that pushes every order that reached
"paid" since the last run to our fulfilment partner's API. The partner creates
one shipment per call and returns a shipment id, which the job stores on the
order. It runs as a Kubernetes CronJob every 10 minutes, on the same cluster
and from the same image as the API, with the partner credentials the API
already has. A normal run finishes in seconds; in staging, the backlog after
a flash sale took about 40 minutes to drain. The on-call engineers watch the
API's dashboards and alerts; finance reconciles shipments against orders once
a week.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
