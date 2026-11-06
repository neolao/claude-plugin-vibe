---
name: review-correctness-scoped-finds-evidence-outside-scope
description: >-
  review-correctness, scoped to fixtures/orders/, must find the shipping
  quote of fixtures/orders/checkout.py dereferenced while
  fixtures/shipping/quotes.py returns None for an unserved country, the
  caller in fixtures/reports/summary.py still passing one argument to
  `discount_rate` of fixtures/orders/pricing.py, the check-then-act of
  fixtures/orders/reservations.py that the thread-pool server of
  fixtures/app/server.py lets overlap, and the trim done in
  fixtures/orders/importer.py while the `normalize_sku` helper of
  fixtures/catalog/sku.py promises it and keeps the defect for its other
  callers — anchoring every finding on a file in scope
tags: [review-correctness, recall, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-correctness` sub-agent (Agent tool, `subagent_type: "vibe:review-correctness"`) to review `fixtures/orders/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/orders/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
