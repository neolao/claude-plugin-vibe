---
name: review-ddd-finds-anemic-service-and-caps-severity
description: >-
  review-ddd must report `RenewalService.renew` in
  fixtures/subscriptions/renewal.py, which decides the subscription's next
  status and period end from the subscription's own fields and writes them
  back through public attributes, as an Anemic model finding naming the
  logic to move onto `Subscription`, and `find_expiring` of
  fixtures/subscriptions/subscription_repository.py handing raw rows to
  fixtures/billing/expiry_notices.py as a Repository finding — and must
  report no finding at `high`
tags: [review-ddd, recall, severity]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-ddd` sub-agent (Agent tool, `subagent_type: "vibe:review-ddd"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

```
Review the code in scope for your dimension only. Read-only: never edit, create, or run anything the agent definition does not explicitly allow.
Report every finding as:

FILE: path/to/file (line N)      — or MODULE:, PACKAGE:, TARGET: when your definition says so
CATEGORY: <one of your categories>
SEVERITY: high | medium | low
ISSUE: what is wrong and why it matters — one or two sentences
SUGGESTION: concrete fix direction — one or two sentences

Severity: high = correctness, security, or a bug that will ship; medium = a clear principle or convention broken; low = minor improvement.
Flag only what you can point to in the code, with a plausible failure or cost — no theoretical findings, no metric-chasing. Skip a category with nothing to report. Do not summarize or count at the end.

Scope: fixtures/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
