---
name: review-tests-scoped-finds-a-changed-test-file-whatever-it-exercises
description: >-
  review-tests, given two changed files (fixtures/billing/invoice.py and
  fixtures/tests/test_rates.py) as its scope, must run the suite, report
  the assertion-free test on test_rates.py although the module it tests
  is out of scope, report the untested empty-invoice branch of invoice.py
  after reading its tests outside the scope, and leave rates.py's own
  untested branch alone
tags: [review-tests, recall, scoped]
runs: 3
max_turns: 10
timeout_seconds: 600
allowed_tools: [Read, Grep, Glob, Agent, Bash]
---

Invoke the `vibe:review-tests` sub-agent (Agent tool, `subagent_type: "vibe:review-tests"`) to review the changed files `fixtures/billing/invoice.py` and `fixtures/tests/test_rates.py` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/billing/invoice.py fixtures/tests/test_rates.py
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its full report back verbatim — including the
`SUITE EXECUTED:` / `E2E/INTEGRATION EXECUTED:` header lines it opens with.
