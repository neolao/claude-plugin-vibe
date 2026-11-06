---
name: expert-ops-new-cache-format-keeps-both-versions-reading
description: >-
  Recall of the deploy-compatibility bullet of expert-ops, in the direction
  the old wording did not name: a service changes the value it stores in a
  shared cache, under the same keys, from a bare number to a structured
  entry, while six pods roll out one at a time and the entries written
  before the rollout live for a day. The expert must require that the old
  pods still read the new entries, that the new pods still read the old
  entries (a new key space, a dual format or tolerant readers), and a
  rollback that holds while new-format entries sit in the cache.
tags: [expert-ops, recall, rolling-deploy]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our catalogue service caches each product's price in the shared Redis
under `price:<sku>`, as a bare number string ("19.90"), for 24 hours; the
checkout reads those keys on every basket. We're going to store a structured
entry instead — the amount, the currency and the date the price is valid
until — so the checkout can show the currency and refuse a stale price. The
catalogue service runs as six pods rolled out one pod at a time through the
usual pipeline; the checkout is deployed separately, by another team, a few
days later. Nothing changes in the database or in the API the checkout calls
when the cache misses.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
