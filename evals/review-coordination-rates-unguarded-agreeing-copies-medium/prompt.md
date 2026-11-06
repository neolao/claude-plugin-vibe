---
name: review-coordination-rates-unguarded-agreeing-copies-medium
description: >-
  review-coordination must rate the free-shipping threshold written as
  `FREE_SHIPPING_THRESHOLD = 50.0` in fixtures/pricing/fees.py and as the
  literal `50.0` in fixtures/web/cart_view.py (equal today, no guard, a
  "keep in sync" comment) `medium` — neither `high` nor `low` — and must
  rate the status list of fixtures/orders/status.py whose copy in
  fixtures/reports/export.py already lacks "cancelled" `high`, with the
  KeyError the export raises on a cancelled order
tags: [review-coordination, recall, severity]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-coordination` sub-agent (Agent tool, `subagent_type: "vibe:review-coordination"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
