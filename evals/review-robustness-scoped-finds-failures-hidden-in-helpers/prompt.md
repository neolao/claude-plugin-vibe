---
name: review-robustness-scoped-finds-failures-hidden-in-helpers
description: >-
  review-robustness, scoped to fixtures/billing/, must find the checkout
  charge reported as done after a rollback that fixtures/db/tx.py swallows,
  the invoice fetch retried forever by fixtures/net/retry.py, and the refund
  failure collapsed into one generic message by fixtures/common/errors.py,
  without flagging the ledger lock that fixtures/locks/held.py releases in a
  finally
tags: [review-robustness, recall, precision, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-robustness` sub-agent (Agent tool, `subagent_type: "vibe:review-robustness"`) to review `fixtures/billing/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/billing/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
