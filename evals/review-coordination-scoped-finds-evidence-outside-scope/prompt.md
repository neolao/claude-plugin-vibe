---
name: review-coordination-scoped-finds-evidence-outside-scope
description: >-
  review-coordination, scoped to fixtures/api/, must report the currency
  list written as `ALLOWED_CURRENCIES` in fixtures/api/handlers.py and as a
  SQL CHECK in fixtures/db/schema.sql, and the export filename format
  produced in fixtures/api/handlers.py and parsed by split("-") in
  fixtures/jobs/archive.py — anchoring both on fixtures/api/handlers.py —
  and must anchor nothing on the retention period written in
  fixtures/jobs/retention.py and fixtures/web/settings_page.py, both
  outside the scope
tags: [review-coordination, recall, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-coordination` sub-agent (Agent tool, `subagent_type: "vibe:review-coordination"`) to review `fixtures/api/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/api/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
