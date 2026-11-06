---
name: review-architecture-rates-a-type-only-cycle-low
description: >-
  review-architecture must not rate above `low` the billing/shipping cycle
  that only a type-only import closes: fixtures/billing/invoice.py imports
  `shipping.schedule` as the map declares, and fixtures/shipping/schedule.py
  names `billing.invoice.Invoice` under `TYPE_CHECKING` for an annotation
  alone — nothing loads or fails, the coupling is the whole cost
tags: [review-architecture, precision, severity]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-architecture` sub-agent (Agent tool, `subagent_type: "vibe:review-architecture"`) to review `fixtures/` in this case directory. `.vibe/` is present at the workspace root, as it is when the internal review runs for real. Give it exactly this prompt:

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
