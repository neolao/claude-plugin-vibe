---
name: review-ddd-leaves-dto-envy-and-names-alone
description: >-
  review-ddd must raise no high or medium finding on `Subscription` of
  fixtures/subscriptions/subscription.py, which guards its own renewal, on
  `to_response` and `SubscriptionResponse` of fixtures/api/presenters.py
  (a boundary shape filled from the entity, never written back), on
  `summarize`, `GatewayPayment` and `InvoiceSummary` of
  fixtures/billing/invoice_summary.py (a function working a gateway export
  row, which is review-antipatterns' feature envy at most, not an anemic
  domain type), nor on the terse helper names `_fmt(d)` and `_label(s)` of
  fixtures/api/presenters.py, whose clarity is review-naming's question
tags: [review-ddd, precision, ownership]
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

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
