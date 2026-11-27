---
name: review-overengineering-scoped-accepts-evidence-outside-scope
description: >-
  review-overengineering, scoped to fixtures/src/notifications/, must raise no
  high or medium finding on the three files in scope (the NotificationChannel
  base class has a second implementation in fixtures/src/sms/sms_channel.py,
  the retry_count parameter is passed 3 and 1 by its two call sites in
  fixtures/src/billing/) and must report nothing on the PricingStrategy base
  class of fixtures/src/billing/pricing.py nor on the currency parameter of
  fixtures/src/billing/money.py — machinery declared outside the scope
tags: [review-overengineering, precision, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-overengineering` sub-agent (Agent tool, `subagent_type: "vibe:review-overengineering"`) to review `fixtures/src/notifications/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/src/notifications/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
