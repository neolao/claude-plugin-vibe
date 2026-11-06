---
name: review-correctness-finds-violations
description: >-
  review-correctness must report the refund rule of fixtures/billing/refunds.py
  that uses `or` where its docstring requires both conditions, the inclusive
  month range of fixtures/billing/periods.py built with an exclusive `range`,
  the receipt recipient of fixtures/billing/notify.py dereferenced after a
  dictionary `get` that misses for a removed customer, the float equality of
  fixtures/billing/settlement.py, the caller in fixtures/reports/summary.py
  that passes one argument to the two-argument `discount_rate`, the unlocked
  check-then-act of fixtures/stock/inventory.py under a thread-pool server,
  and the SKU trim done at one call site (fixtures/catalog/importer.py)
  while the shared `normalize_sku` helper of fixtures/catalog/sku.py keeps
  the defect for its other callers — each with a SCENARIO line
tags: [review-correctness, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-correctness` sub-agent (Agent tool, `subagent_type: "vibe:review-correctness"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
