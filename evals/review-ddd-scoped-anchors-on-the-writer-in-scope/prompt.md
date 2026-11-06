---
name: review-ddd-scoped-anchors-on-the-writer-in-scope
description: >-
  review-ddd, scoped to fixtures/promotions/, must report `apply_bundle`
  of fixtures/promotions/bundles.py appending to `order._lines` of the
  `Order` aggregate defined in fixtures/orders/order.py (outside the scope)
  as an Aggregate finding anchored on bundles.py that names `add_line`, and
  must report nothing anchored outside fixtures/promotions/ — the raw rows
  of fixtures/dunning/reminders.py, the address edited in place by
  fixtures/orders/order.py and the buyer of fixtures/orders/ have both ends
  outside the scope
tags: [review-ddd, recall, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-ddd` sub-agent (Agent tool, `subagent_type: "vibe:review-ddd"`) to review `fixtures/promotions/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/promotions/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
