---
name: review-antipatterns-flags-shape-of-superseded-decision
description: >-
  review-antipatterns must flag the module-level `HANDLERS` dict of
  fixtures/shop/handlers/__init__.py as mutable global state, naming a
  writer (fixtures/shop/handlers/billing.py, shipping.py or
  fixtures/shop/admin.py), although
  `.vibe/decisions/001-import-time-handler-registry.md` once mandated it —
  that decision is superseded by 002, which retires the registry — and must
  flag the unread `QUEUE_*` constants of fixtures/shop/config.py as cargo
  cult (no framework and no repo code reads them)
tags: [review-antipatterns, recall, decisions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-antipatterns` sub-agent (Agent tool, `subagent_type: "vibe:review-antipatterns"`) to review `fixtures/` in this case directory. `.vibe/` is present at the workspace root, as it is when `/vibe:feature` runs the review for real. Give it exactly this prompt:

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
