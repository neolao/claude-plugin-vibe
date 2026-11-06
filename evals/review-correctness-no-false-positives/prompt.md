---
name: review-correctness-no-false-positives
description: >-
  review-correctness must raise no high or medium finding on the receipt
  recipient of fixtures/billing/notify.py whose only caller validates the
  customer first, on the exclusive month range of fixtures/billing/periods.py
  whose docstring says the end is excluded, on `discount_rate` whose every
  caller passes both arguments, on the stock reservation of
  fixtures/stock/inventory.py held under a lock, on the tolerance-based
  settlement check of fixtures/billing/settlement.py, on the cent truncation
  of fixtures/billing/rounding.py that an accepted decision in .vibe/decisions/
  mandates, nor on the explicitly fire-and-forget audit task of
  fixtures/billing/audit.py
tags: [review-correctness, precision]
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

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
