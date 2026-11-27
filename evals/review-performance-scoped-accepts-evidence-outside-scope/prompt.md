---
name: review-performance-scoped-accepts-evidence-outside-scope
description: >-
  review-performance, scoped to fixtures/shipping/, must raise no high or
  medium finding on the helpers in scope (the per-call carrier query of
  presenters.py is called once per detail request and the list handler uses
  the join, the sync wkhtmltopdf call of labels.py runs in a thread, the
  linear district scan of zones.py runs three times at startup, the scan
  store of tracking.py is pruned by a nightly job in fixtures/api/jobs.py)
  and must report nothing on the N+1 that sits wholly in
  fixtures/api/reports.py
tags: [review-performance, precision, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-performance` sub-agent (Agent tool, `subagent_type: "vibe:review-performance"`) to review `fixtures/shipping/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/shipping/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
