---
name: review-coordination-finds-violations
description: >-
  review-coordination must report the overdue rule written in
  fixtures/tickets/model.py and restated in fixtures/reports/overdue.py,
  the priority list of fixtures/tickets/priority.py copied in
  fixtures/web/static/priority.js (the backend test compares PRIORITIES
  with SLA_HOURS only, which guards nothing between the two tiers), and the
  attachment limit written as MAX_ATTACHMENTS in fixtures/tickets/limits.py
  and as the literal 5 under a "keep in sync" comment in
  fixtures/web/upload_form.py
tags: [review-coordination, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-coordination` sub-agent (Agent tool, `subagent_type: "vibe:review-coordination"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
