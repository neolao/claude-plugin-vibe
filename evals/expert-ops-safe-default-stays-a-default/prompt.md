---
name: expert-ops-safe-default-stays-a-default
description: >-
  Precision side of the default rule in expert-ops's config bullet: an
  export job gains two tunables, a per-call timeout and a batch size,
  each with a default the brief has measured to be right in production,
  and nothing about where the job writes or authenticates changes. The
  expert must not make either value required, demand it be set per
  environment or ask the Product Owner about it: a default that is safe
  in production stays a default, and the lists go to what the job's
  change actually risks.
tags: [expert-ops, precision, config-defaults]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our nightly export job sends the day's orders to the accounting tool's API,
one call per batch, and has run as a Kubernetes CronJob for two years; its
endpoint and credentials come from the existing secret and do not change.
The accounting tool now times out on large batches, so we're making two
values tunable through the existing `config` module, which reads
environment variables with a default: the per-call timeout, defaulting to
the 30 seconds the job has always used, and the batch size, defaulting to
the 500 orders a week of production runs showed never times out. Both
defaults are the values production runs with today; the variables exist so
the on-call engineer can lower them during an incident without a deploy.
Nothing else in the job, its schedule, its image or its alerting changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
