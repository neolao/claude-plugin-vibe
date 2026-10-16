---
name: review-dependencies-scoped-accepts-evidence-outside-scope
description: review-dependencies, scoped to fixtures/orders/, must not call unused or misplaced the dependencies whose only importers sit outside the scope (httpx, tabulate, python-dateutil as dateutil, freezegun in the dev extra) nor pytest-cov, never imported but named in the pytest options of fixtures/pyproject.toml
tags: [review-dependencies, precision, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent, Bash]
---

Invoke the `vibe:review-dependencies` sub-agent (Agent tool, `subagent_type: "vibe:review-dependencies"`) to review `fixtures/orders/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/orders/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
