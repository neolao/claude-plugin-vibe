---
name: review-architecture-flags-drift-despite-a-stale-map
description: >-
  review-architecture must still report, in a stale `.vibe/` map, the drift
  a sync would not erase: fixtures/core/discounts.py, which the core
  module's `Files:` list omits, opens a Postgres connection and imports
  `adapters.config` against the declared direction and the role; the
  unmapped zone fixtures/notifications/ closes a cycle with `core`
  (fixtures/core/order_service.py imports `notifications.templates`, the
  notifier imports `core.ports`); fixtures/core/pricing.py computes VAT in
  float arithmetic against the accepted decision
  `.vibe/decisions/002-money-in-integer-cents.md`, whose finding must offer
  both ways out — while the `reports` module whose listed file is gone is
  not an orphan
tags: [review-architecture, recall, stale-map]
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

Once the sub-agent returns, report its findings back verbatim.
