---
name: review-web-security-scoped-accepts-evidence-outside-scope
description: >-
  review-web-security, scoped to fixtures/portal/routes/, must not flag the
  download route whose outside storage helper contains the name, the delete
  route the outside login hook guards with an admin role check, or the
  order route whose outside renderer filters on the owner, must anchor
  nothing outside fixtures/portal/routes/, and must never report the
  uncapped export that sits wholly in fixtures/portal/app.py
tags: [review-web-security, precision, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-web-security` sub-agent (Agent tool, `subagent_type: "vibe:review-web-security"`) to review `fixtures/portal/routes/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/portal/routes/
Dynamic verification: not enabled — static review only, do not launch or probe any server.
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
