---
name: review-performance-scoped-finds-evidence-outside-scope
description: >-
  review-performance, scoped to fixtures/shipping/, must find the per-shipment
  carrier query of presenters.py that api/app.py loops, the synchronous
  wkhtmltopdf call of labels.py that an async handler reaches, the linear
  district scan of zones.py that the bulk quote handler drives 5 000 times per
  call, and the scan store of tracking.py that the carrier webhook feeds and
  nothing prunes — anchoring every finding on a file under fixtures/shipping/
  and leaving alone the N+1 that sits wholly in fixtures/api/reports.py
tags: [review-performance, recall, scoped]
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

Once the sub-agent returns, report its findings back verbatim.
