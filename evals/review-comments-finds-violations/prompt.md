---
name: review-comments-finds-violations
description: >-
  review-comments must report, in fixtures/ledger/, the `# add the amount to
  the balance` comment of accounts.py as Redundant, the three-line overdraft
  comment of accounts.py as Verbose with a shorter version, the `# withdraw
  first ...; amount in cents` comment of transfer.py as Partially redundant
  keeping the order reason, and the `# business days` comment on
  `SETTLEMENT_DELAY` in transfer.py as Misleading at `high`, citing the
  `date.today() + SETTLEMENT_DELAY` line that adds calendar days
tags: [review-comments, recall]
runs: 3
max_turns: 10
timeout_seconds: 600
allowed_tools: [Read, Grep, Glob, Agent, Bash]
---

Invoke the `vibe:review-comments` sub-agent (Agent tool, `subagent_type: "vibe:review-comments"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
