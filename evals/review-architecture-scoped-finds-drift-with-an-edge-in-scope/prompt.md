---
name: review-architecture-scoped-finds-drift-with-an-edge-in-scope
description: >-
  review-architecture, scoped to the two changed files
  fixtures/core/events.py and fixtures/metrics/collector.py, must report the
  core/adapters cycle that fixtures/core/events.py closes by importing
  fixtures/adapters/audit_log.py (the other end sits outside the scope,
  named as evidence) and the `metrics` module nothing imports (its only
  file is in scope), with the module finding citing the file path — while
  leaving the orphaned `reporting` module and the adapter-to-adapter call in
  fixtures/adapters/postgres_gateway.py, which no in-scope file takes part
  in, to the full review
tags: [review-architecture, recall, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-architecture` sub-agent (Agent tool, `subagent_type: "vibe:review-architecture"`) to review the two changed files `fixtures/core/events.py` and `fixtures/metrics/collector.py` in this case directory. `.vibe/` is present at the workspace root, as it is when `/vibe:feature` runs the review for real. Give it exactly this prompt:

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

Scope: fixtures/core/events.py, fixtures/metrics/collector.py
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
