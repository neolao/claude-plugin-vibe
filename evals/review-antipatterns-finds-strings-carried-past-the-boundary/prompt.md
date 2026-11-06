---
name: review-antipatterns-finds-strings-carried-past-the-boundary
description: >-
  review-antipatterns must flag the `APP_ENV` string that
  fixtures/cli/main.py reads and passes unparsed to fixtures/cli/export.py,
  fixtures/cli/storage.py and fixtures/cli/alerts.py, each comparing it to
  "production" or "staging" literals, as stringly-typed code, and
  `CheckoutFacade` in fixtures/checkout/facade.py — named as a facade but
  performing every step of the checkout inline itself — as a god object
tags: [review-antipatterns, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-antipatterns` sub-agent (Agent tool, `subagent_type: "vibe:review-antipatterns"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
