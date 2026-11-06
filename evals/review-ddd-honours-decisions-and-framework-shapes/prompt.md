---
name: review-ddd-honours-decisions-and-framework-shapes
description: >-
  review-ddd must raise no high or medium finding on the `buyer` that
  fixtures/api/routes.py keeps in its path and payload (the accepted
  `.vibe/decisions/001-buyer-kept-in-public-api.md` mandates it), on the
  public SQLAlchemy relationship `Product.variants` of
  fixtures/catalog/models.py (the ORM requires it, and the only writer
  goes through `add_variant`), on `OrderRow` of fixtures/orders/persistence.py
  (a persistence shape beside the domain type), on the `ShopPreferences`
  CRUD module of fixtures/settings/ that holds no rule, nor on the
  `OrderPlaced` event that fixtures/checkout/place_order.py hands
  synchronously to the inventory handler
tags: [review-ddd, precision, decisions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-ddd` sub-agent (Agent tool, `subagent_type: "vibe:review-ddd"`) to review `fixtures/` in this case directory. `.vibe/` is present at the workspace root, as it is when `/vibe:feature` runs the review for real. Give it exactly this prompt:

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
