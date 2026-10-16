---
name: review-tests-scoped-accepts-tests-outside-scope
description: review-tests, scoped to fixtures/src/billing/, must run the suite configured in fixtures/package.json and must not call the in-scope module untested because its sound tests live in fixtures/tests/, nor flag the awaited async tests, nor report the tests of fixtures/src/shipping/
tags: [review-tests, precision, scoped]
runs: 3
max_turns: 10
timeout_seconds: 600
allowed_tools: [Read, Grep, Glob, Agent, Bash]
---

Invoke the `vibe:review-tests` sub-agent (Agent tool, `subagent_type: "vibe:review-tests"`) to review `fixtures/src/billing/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/src/billing/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its full report back verbatim — including the
`SUITE EXECUTED:` / `E2E/INTEGRATION EXECUTED:` header lines — or state that it found nothing.
